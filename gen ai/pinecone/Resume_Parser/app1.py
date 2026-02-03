# =========================================================
# STEP 1: Imports
# =========================================================
import os
import time
import pandas as pd
from functools import lru_cache
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec, CloudProvider, AwsRegion, Metric


# =========================================================
# STEP 2: Load Embedding Model (FIRST)
# =========================================================
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
EMBEDDING_DIM = model.get_sentence_embedding_dimension()
print("Embedding dimension:", EMBEDDING_DIM)

# Warm up model (kills cold start)
model.encode("warmup sentence")


# =========================================================
# STEP 3: Initialize Pinecone
# =========================================================
PINECONE_API_KEY = "pcsk_28KAeR_HiRv9q9SWM5ytThT3ry3jD8FJK9CBH6HYuviyQWzCwM3JY9W1rAojotCzNgKNH5"
INDEX_NAME = "latency-seconds-index"

pc = Pinecone(api_key=PINECONE_API_KEY)

# Clean start (OK for experiments)
if pc.has_index(INDEX_NAME):
    pc.delete_index(INDEX_NAME)

pc.create_index(
    name=INDEX_NAME,
    dimension=EMBEDDING_DIM,
    metric=Metric.COSINE,
    spec=ServerlessSpec(
        cloud=CloudProvider.AWS,
        region=AwsRegion.US_EAST_1
    )
)

print("Waiting for index to be ready...")
while not pc.describe_index(INDEX_NAME).status["ready"]:
    time.sleep(2)

index_host = pc.describe_index(INDEX_NAME).host
index = pc.Index(host=index_host)
print("Index ready")


# =========================================================
# STEP 4: Read PDFs (LIMIT = 1000)
# =========================================================
PDF_FOLDER = "Education"

def read_pdfs(folder, limit=1000):
    documents = {}
    count = 0

    for file in sorted(os.listdir(folder)):
        if file.lower().endswith(".pdf"):
            if count >= limit:
                break

            reader = PdfReader(os.path.join(folder, file))
            text = ""

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "

            if text.strip():
                documents[f"doc_{count}"] = {
                    "text": text,
                    "file_name": file
                }
                count += 1

    return documents


start = time.time()
documents = read_pdfs(PDF_FOLDER)
print(f"PDFs loaded: {len(documents)}")
print(f"PDF read time: {time.time() - start:.2f} seconds")


# =========================================================
# STEP 5: Chunking
# =========================================================
def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)

    return chunks


# =========================================================
# STEP 6: Create Embeddings + Metadata
# =========================================================
vectors = []

start = time.time()
for doc_id, doc in documents.items():
    chunks = chunk_text(doc["text"])

    for i, chunk in enumerate(chunks):
        embedding = model.encode(
            chunk,
            normalize_embeddings=True
        ).tolist()

        vectors.append((
            f"{doc_id}_chunk_{i}",
            embedding,
            {
                "doc_id": doc_id,
                "file_name": doc["file_name"]
            }
        ))

print(f"Total vectors created: {len(vectors)}")
print(f"Embedding time: {time.time() - start:.2f} seconds")


# =========================================================
# STEP 7: Upsert Vectors (SAFE BATCHING)
# =========================================================
BATCH_SIZE = 50

for i in range(0, len(vectors), BATCH_SIZE):
    index.upsert(vectors=vectors[i:i + BATCH_SIZE])

print("Upsert completed")


# =========================================================
# STEP 8: Cached Query Embedding (CRITICAL)
# =========================================================
@lru_cache(maxsize=100)
def get_query_embedding(query: str):
    return model.encode(
        query,
        normalize_embeddings=True
    ).tolist()


# =========================================================
# STEP 9: Search Methods (RETURN SECONDS)
# =========================================================
QUERY = "data engineer azure databricks"

# 1️⃣ Baseline (no cache usage inside function)
def search_baseline():
    q_emb = model.encode(QUERY).tolist()
    start = time.time()
    index.query(vector=q_emb, top_k=5)
    return time.time() - start


# 2️⃣ Warm model
def search_warm():
    q_emb = model.encode(QUERY).tolist()
    start = time.time()
    index.query(vector=q_emb, top_k=5)
    return time.time() - start


# 3️⃣ Cached embedding
def search_cached():
    q_emb = get_query_embedding(QUERY)
    start = time.time()
    index.query(vector=q_emb, top_k=5)
    return time.time() - start


# 4️⃣ Cached + metadata filter
def search_filtered():
    q_emb = get_query_embedding(QUERY)
    start = time.time()
    index.query(
        vector=q_emb,
        top_k=5,
        filter={"doc_id": {"$exists": True}}
    )
    return time.time() - start


# 5️⃣ Best (cached + filter + minimal payload)
def search_best():
    q_emb = get_query_embedding(QUERY)
    start = time.time()
    index.query(
        vector=q_emb,
        top_k=5,
        include_metadata=False,
        include_values=False,
        filter={"doc_id": {"$exists": True}}
    )
    return time.time() - start


# =========================================================
# STEP 10: Run Experiments
# =========================================================
results = []

for _ in range(5):
    results.append({"method": "baseline", "latency_sec": search_baseline()})
    results.append({"method": "warm", "latency_sec": search_warm()})
    results.append({"method": "cached", "latency_sec": search_cached()})
    results.append({"method": "filtered", "latency_sec": search_filtered()})
    results.append({"method": "best", "latency_sec": search_best()})


# =========================================================
# STEP 11: Final Latency Table (SECONDS)
# =========================================================
df = pd.DataFrame(results)

print("\n===== LATENCY COMPARISON (SECONDS) =====")
print(df.groupby("method").mean())
