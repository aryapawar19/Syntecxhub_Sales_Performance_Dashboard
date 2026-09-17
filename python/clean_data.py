import pandas as pd

# Load raw dataset
input_file = "data/raw/sales_raw.xls"

df = pd.read_excel(input_file)

print("Original shape:", df.shape)

# Clean column names
df.columns = df.columns.str.strip()

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Remove completely empty rows
df = df.dropna(how="all")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing critical values
critical_columns = [
    "Order ID",
    "Order Date",
    "Product ID",
    "Product Name",
    "Sales",
    "Profit"
]

df = df.dropna(subset=critical_columns)

# Create time-based columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.strftime("%B")
df["Quarter"] = "Q" + df["Order Date"].dt.quarter.astype(str)

# Sort by order date
df = df.sort_values("Order Date")

# Save cleaned dataset
output_file = "data/cleaned/sales_cleaned.csv"
df.to_csv(output_file, index=False)

print("Cleaned shape:", df.shape)
print("Cleaned dataset saved to:", output_file)
print("\nCleaning completed successfully!")