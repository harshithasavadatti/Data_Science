import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings

warnings.filterwarnings("ignore")

# =============================================================================
# STYLE & PALETTE
# =============================================================================
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 10

PALETTE = {
    "no_churn": "#2ecc71",
    "churn": "#e74c3c",
    "primary": "#3498db",
    "secondary": "#9b59b6",
    "accent": "#f39c12"
}

CHURN_COLORS = [PALETTE["no_churn"], PALETTE["churn"]]
sns.set_palette(CHURN_COLORS)

# =============================================================================
# LOAD DATA
# =============================================================================
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

output_dir = Path("eda_graphs")
output_dir.mkdir(exist_ok=True)

# =============================================================================
# 1. CHURN DISTRIBUTION (PIE)
# =============================================================================
df["Churn"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    colors=CHURN_COLORS
)
plt.title("Customer Churn Distribution")
plt.ylabel("")
plt.savefig(output_dir / "01_churn_distribution.png", dpi=300)
plt.close()

# =============================================================================
# 2. CHURN COUNT
# =============================================================================
sns.countplot(data=df, x="Churn", palette=CHURN_COLORS)
plt.title("Customer Churn Count")
plt.savefig(output_dir / "02_churn_count.png", dpi=300)
plt.close()

# =============================================================================
# 3. GENDER VS CHURN
# =============================================================================
pd.crosstab(df["gender"], df["Churn"]).plot(
    kind="bar", color=CHURN_COLORS, edgecolor="black"
)
plt.title("Gender vs Churn")
plt.xticks(rotation=0)
plt.savefig(output_dir / "03_gender_churn.png", dpi=300)
plt.close()

# =============================================================================
# 4. SENIOR CITIZEN VS CHURN
# =============================================================================
df["SeniorCitizen"] = df["SeniorCitizen"].map({0: "No", 1: "Yes"})
pd.crosstab(df["SeniorCitizen"], df["Churn"]).plot(
    kind="bar", color=CHURN_COLORS, edgecolor="black"
)
plt.title("Senior Citizen vs Churn")
plt.xticks(rotation=0)
plt.savefig(output_dir / "04_senior_citizen_churn.png", dpi=300)
plt.close()

# =============================================================================
# 5. PARTNER & DEPENDENTS
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

pd.crosstab(df["Partner"], df["Churn"]).plot(
    kind="bar", ax=axes[0], color=CHURN_COLORS, edgecolor="black"
)
axes[0].set_title("Partner vs Churn")

pd.crosstab(df["Dependents"], df["Churn"]).plot(
    kind="bar", ax=axes[1], color=CHURN_COLORS, edgecolor="black"
)
axes[1].set_title("Dependents vs Churn")

plt.tight_layout()
plt.savefig(output_dir / "05_partner_dependents.png", dpi=300)
plt.close()

# =============================================================================
# 6. TENURE DISTRIBUTION
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

axes[0].hist(df["tenure"], bins=40,
             color=PALETTE["primary"], edgecolor="black")
axes[0].set_title("Tenure Distribution")

df.boxplot(column="tenure", by="Churn", ax=axes[1])
axes[1].set_title("Tenure by Churn")
plt.suptitle("")

plt.savefig(output_dir / "06_tenure_distribution.png", dpi=300)
plt.close()

# =============================================================================
# 7. MONTHLY CHARGES
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

axes[0].hist(df["MonthlyCharges"], bins=40,
             color=PALETTE["secondary"], edgecolor="black")
axes[0].set_title("Monthly Charges Distribution")

df.boxplot(column="MonthlyCharges", by="Churn", ax=axes[1])
axes[1].set_title("Monthly Charges by Churn")
plt.suptitle("")

plt.savefig(output_dir / "07_monthly_charges.png", dpi=300)
plt.close()

# =============================================================================
# 8. TOTAL CHARGES
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

df["TotalCharges"].dropna().hist(
    bins=40, ax=axes[0],
    color=PALETTE["accent"], edgecolor="black"
)
axes[0].set_title("Total Charges Distribution")

df.dropna(subset=["TotalCharges"]).boxplot(
    column="TotalCharges", by="Churn", ax=axes[1]
)
axes[1].set_title("Total Charges by Churn")
plt.suptitle("")

plt.savefig(output_dir / "08_total_charges.png", dpi=300)
plt.close()

# =============================================================================
# 9. CONTRACT TYPE
# =============================================================================
pd.crosstab(df["Contract"], df["Churn"]).plot(
    kind="bar", color=CHURN_COLORS, edgecolor="black"
)
plt.title("Contract Type vs Churn")
plt.xticks(rotation=45)
plt.savefig(output_dir / "09_contract_churn.png", dpi=300)
plt.close()

# =============================================================================
# 10. PAYMENT METHOD
# =============================================================================
pd.crosstab(df["PaymentMethod"], df["Churn"]).plot(
    kind="bar", color=CHURN_COLORS, edgecolor="black"
)
plt.title("Payment Method vs Churn")
plt.xticks(rotation=45)
plt.savefig(output_dir / "10_payment_method_churn.png", dpi=300)
plt.close()

# =============================================================================
# 11. INTERNET SERVICE
# =============================================================================
pd.crosstab(df["InternetService"], df["Churn"]).plot(
    kind="bar", color=CHURN_COLORS, edgecolor="black"
)
plt.title("Internet Service vs Churn")
plt.savefig(output_dir / "11_internet_service_churn.png", dpi=300)
plt.close()

# =============================================================================
# 12. SERVICE FEATURES GRID
# =============================================================================
features = [
    "PhoneService", "MultipleLines", "OnlineSecurity", "OnlineBackup",
    "DeviceProtection", "TechSupport", "StreamingTV",
    "StreamingMovies", "PaperlessBilling"
]

fig, axes = plt.subplots(3, 3, figsize=(18, 15))
axes = axes.flatten()

for i, f in enumerate(features):
    pd.crosstab(df[f], df["Churn"]).plot(
        kind="bar", ax=axes[i],
        color=CHURN_COLORS, edgecolor="black"
    )
    axes[i].set_title(f)
    axes[i].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig(output_dir / "12_service_features.png", dpi=300)
plt.close()

# =============================================================================
# 13. CORRELATION HEATMAP
# =============================================================================
corr = df.select_dtypes(include=np.number).corr()
sns.heatmap(corr, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig(output_dir / "13_correlation_heatmap.png", dpi=300)
plt.close()

# =============================================================================
# 14. TENURE VS MONTHLY CHARGES
# =============================================================================
plt.scatter(df[df["Churn"] == "No"]["tenure"],
            df[df["Churn"] == "No"]["MonthlyCharges"],
            color=PALETTE["no_churn"], alpha=0.5, label="No Churn")
plt.scatter(df[df["Churn"] == "Yes"]["tenure"],
            df[df["Churn"] == "Yes"]["MonthlyCharges"],
            color=PALETTE["churn"], alpha=0.5, label="Churn")
plt.legend()
plt.title("Tenure vs Monthly Charges")
plt.savefig(output_dir / "14_tenure_vs_monthly_charges.png", dpi=300)
plt.close()

# =============================================================================
# 15. CHURN RATE BY CONTRACT
# =============================================================================
(df.groupby("Contract")["Churn"]
 .apply(lambda x: (x == "Yes").mean() * 100)
 .plot(kind="bar", color=PALETTE["churn"], edgecolor="black"))
plt.title("Churn Rate by Contract (%)")
plt.savefig(output_dir / "15_churn_rate_contract.png", dpi=300)
plt.close()

# =============================================================================
# 16. CHURN RATE BY PAYMENT METHOD
# =============================================================================
(df.groupby("PaymentMethod")["Churn"]
 .apply(lambda x: (x == "Yes").mean() * 100)
 .plot(kind="bar", color=PALETTE["churn"], edgecolor="black"))
plt.title("Churn Rate by Payment Method (%)")
plt.savefig(output_dir / "16_churn_rate_payment.png", dpi=300)
plt.close()

# =============================================================================
# 17. NUMERIC DISTRIBUTIONS BY CHURN
# =============================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for i, col in enumerate(["tenure", "MonthlyCharges", "TotalCharges"]):
    axes[i].hist(df[df["Churn"] == "No"][col].dropna(),
                 alpha=0.6, color=PALETTE["no_churn"], label="No Churn")
    axes[i].hist(df[df["Churn"] == "Yes"][col].dropna(),
                 alpha=0.6, color=PALETTE["churn"], label="Churn")
    axes[i].set_title(col)
    axes[i].legend()

plt.tight_layout()
plt.savefig(output_dir / "17_numeric_distributions.png", dpi=300)
plt.close()

print("✅ ALL 17 GRAPHS GENERATED USING YOUR CUSTOM PALETTE")
