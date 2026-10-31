import pandas as pd
import numpy as np

# Creating a sample dataset with intentional quality issues
raw_data = {
    'Order_ID': [101, 102, 103, 104, 104, 105, 106, 107],
    'Order_Date': ['2023-01-15', '2023-01-16', 'INVALID_DATE', '2023-01-18', '2023-01-18', '2023-01-19', '2023-01-20', '2023-01-21'],
    'Region': [' North ', 'South', 'East', ' West', ' West', 'North', 'South', 'East'],
    'Category': ['electronics', 'Furniture', 'ELECTRONICS', 'furniture', 'furniture', 'Office Supplies', 'furniture', 'Office Supplies'],
    'Sales': [250.0, np.nan, 150.5, 400.0, 400.0, 75.0, 300.0, 120.0],
    'Quantity': [2, 1, -3, 4, 4, 5, 2, 1]
}

df_raw = pd.DataFrame(raw_data)
df_raw.to_csv('sales_data.csv', index=False)

# 1. Load and Explore
df = pd.read_csv('sales_data.csv')

print("=== HEAD ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

print("\n=== DESCRIBE ===")
print(df.describe(include='all'))

print("\n=== SHAPE ===")
print(df.shape)

# Cleaning operations
df['Sales'] = df['Sales'].fillna(df['Sales'].median())
df = df.drop_duplicates()
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
df['Region'] = df['Region'].astype(str).str.strip()
df['Category'] = df['Category'].astype(str).str.strip().str.title()
df['Quantity'] = df['Quantity'].abs()

print("=== CLEANED DATA INFO ===")
print(df.info())
print("\n=== CLEANED DATASET ===")
print(df)




# Aggregate total sales by Region
region_sales = df.groupby('Region')['Sales'].sum().reset_index()

print("=== TOTAL SALES BY REGION ===")
print(region_sales)


# Pivot table summarizing Sales by Region and Category
sales_pivot = df.pivot_table(
    index='Region', 
    columns='Category', 
    values='Sales', 
    aggfunc='sum', 
    fill_value=0
)

print("=== PIVOT TABLE: SALES BY REGION & CATEGORY ===")
print(sales_pivot)


# Export cleaned dataset
df.to_csv('cleaned_data.csv', index=False)
print("Dataset successfully saved to cleaned_data.csv")
