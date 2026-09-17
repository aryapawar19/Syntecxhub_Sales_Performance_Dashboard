import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned/sales_cleaned.csv")

# Yearly performance
yearly = (
    df.groupby("Year")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)

yearly["Sales Growth %"] = yearly["Sales"].pct_change() * 100

# Category performance
category = (
    df.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)

# Region performance
region = (
    df.groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)

# Product performance
product = (
    df.groupby("Product Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)

# Top products
top_sales = product.sort_values("Sales", ascending=False).head(10)
top_profit = product.sort_values("Profit", ascending=False).head(10)

# Low-profit products
low_profit = product.sort_values("Profit").head(10)

# Create Excel summary
output_file = "data/cleaned/sales_analysis_summary.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    yearly.to_excel(
        writer,
        sheet_name="Yearly Performance",
        index=False
    )

    category.to_excel(
        writer,
        sheet_name="Category Performance",
        index=False
    )

    region.to_excel(
        writer,
        sheet_name="Region Performance",
        index=False
    )

    top_sales.to_excel(
        writer,
        sheet_name="Top Sales Products",
        index=False
    )

    top_profit.to_excel(
        writer,
        sheet_name="Top Profit Products",
        index=False
    )

    low_profit.to_excel(
        writer,
        sheet_name="Low Profit Products",
        index=False
    )

print("======================================")
print("ANALYSIS SUMMARY CREATED SUCCESSFULLY")
print("======================================")
print(f"File saved to: {output_file}")
print()
print("Sheets created:")
print("1. Yearly Performance")
print("2. Category Performance")
print("3. Region Performance")
print("4. Top Sales Products")
print("5. Top Profit Products")
print("6. Low Profit Products")