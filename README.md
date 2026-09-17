# Sales Performance Dashboard

## Syntecxhub Internship - Task 1

This project is a Sales Performance Dashboard created as part of my Data Analysis internship at Syntecxhub.

## Project Objective

The objective of this project is to analyze sales data and create an interactive dashboard that provides insights into:

- Overall sales and profit performance
- Monthly and yearly sales trends
- Sales performance by category
- Sales performance by region
- Top-selling products
- Low-profit products
- Key performance indicators (KPIs)

## Tools & Technologies

- Python
- Pandas
- NumPy
- Power BI
- Excel
- Git & GitHub

## Dataset

The project uses the Sample Superstore sales dataset.

The raw dataset was cleaned using Python before being imported into Power BI.

## Data Cleaning

The following steps were performed:

- Removed completely empty rows
- Removed duplicate records
- Checked missing values
- Validated important columns
- Converted date columns into proper date format
- Added Year
- Added Month
- Added Month Name
- Added Quarter

## Key Performance Indicators

- Total Sales: 2.33M
- Total Profit: 292.30K
- Sales Growth: 21.44%
- Profit Margin: 12.56%

## Dashboard Features

The Power BI dashboard includes:

- Total Sales KPI
- Total Profit KPI
- Sales Growth KPI
- Profit Margin KPI
- Yearly Sales Trend
- Monthly Sales Trend
- Sales by Category
- Sales by Region
- Top 10 Products by Sales
- Low-Profit Products
- Year, Region and Category filters

## Project Structure

```text
Task1_Sales_Performance_Dashboard/
│
├── data/
│   ├── raw/
│   │   └── sales_raw.xls
│   └── cleaned/
│       └── sales_cleaned.csv
│
├── python/
│   └── clean_data.py
│
├── powerbi/
│   └── Syntecxhub_Sales_Performance_Dashboard.pbix
│
├── screenshots/
│
└── README.md