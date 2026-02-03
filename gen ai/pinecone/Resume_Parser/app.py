import os
import time
from pypdf import PdfReader
from pinecone import Pinecone, ServerlessSpec, CloudProvider, AwsRegion, Metric
from sentence_transformers import SentenceTransformer

# ---------------------------------------------------------
# Load Embedding Model
# ---------------------------------------------------------
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embedding_dim = model.get_sentence_embedding_dimension()
print("Embedding dimension:", embedding_dim)

# ---------------------------------------------------------
# Initialize Pinecone
# ---------------------------------------------------------
api_key = "API_KEY   # ⚠️ move to env variable in real projects
pc = Pinecone(api_key=api_key)

index_name = "resume-search-index"

# Delete index if exists
if pc.has_index(index_name):
    pc.delete_index(index_name)

# Create index
pc.create_index(
    name=index_name,
    dimension=embedding_dim,
    metric=Metric.COSINE,
    spec=ServerlessSpec(
        cloud=CloudProvider.AWS,
        region=AwsRegion.US_EAST_1
    )
)

index = pc.Index(host=pc.describe_index(index_name).host)
print("Index created successfully")

# ---------------------------------------------------------
# PDF Text Extraction
# ---------------------------------------------------------
pdf_folder_path = r"Education"

def extract_text_from_pdfs(folder_path):
    documents = {}
    doc_id = 1

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, file_name)
            reader = PdfReader(file_path)

            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "

            if text.strip():
                documents[f"doc_{doc_id}"] = text
                doc_id += 1

    return documents

start_time = time.time()
documents = extract_text_from_pdfs(pdf_folder_path)
end_time = time.time()

print(f"Text extraction completed in {end_time - start_time:.2f} seconds")
print(f"Total documents loaded: {len(documents)}")

# ---------------------------------------------------------
# Generate Embeddings
# ---------------------------------------------------------
doc_ids = list(documents.keys())
doc_texts = list(documents.values())

embeddings = model.encode(
    doc_texts,
    batch_size=16,
    show_progress_bar=True
).tolist()

vectors = list(zip(doc_ids, embeddings))

# ---------------------------------------------------------
# Upsert into Pinecone
# ---------------------------------------------------------
index.upsert(vectors=vectors)

# ---------------------------------------------------------
# Wait Until Indexing Completes
# ---------------------------------------------------------
def wait_until_indexing_complete(idx, expected_count, check_interval=5):
    while True:
        stats = idx.describe_index_stats()
        current_count = stats.total_vector_count
        print(f"Indexed: {current_count}/{expected_count}")
        if current_count >= expected_count:
            break
        time.sleep(check_interval)

wait_until_indexing_complete(index, len(documents))

# ---------------------------------------------------------
# Semantic Queries
# ---------------------------------------------------------
query_text1 = "data engineering resume, azure data factory, azure databricks"
query_text2 = "data science machine learning langchain gen ai agentic ai"

query_embedding = model.encode(query_text1).tolist()

results = index.query(
    vector=query_embedding,
    top_k=5,
    include_values=False
)

print("\nSearch Results:")
print(results)

