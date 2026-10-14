

import pandas as pd
import matplotlib.pyplot as plt

print("=== 1. Loading the Dataset ===")
#loading the dataset
df = pd.read_csv('sales_data.csv')

# displaying the first 5 rows to check if it loaded correctly
print(df.head())


print("\n... 2. Cleaning the Data ...")
# Check for missing values and remove them
print("Missing values before cleaning:")
print(df.isnull().sum())

df = df.dropna()
print("Data cleaned successfully!")


print("\n=== 3. Calculating Total Revenue ===")
# Multiply quantity by unit price to get total sales for each row
df['Total_Sales'] = df['quantity'] * df['price']

# Find the overall total revenue
total_revenue = df['Total_Sales'].sum()
print(f"Total Revenue of the Company: ${total_revenue:,.2f}")


print("\n=== 4. Finding Top-Selling Products ===")
# Group by product name and sum up the quantities sold
top_products = df.groupby('product')['quantity'].sum().reset_index()

# Sort to find the highest selling products first
top_products = top_products.sort_values(by='quantity', ascending=False)
print(top_products.head())


print("\n=== 5. Creating Charts ===")

# Chart 1: Simple Bar Chart for Top Products
plt.figure(figsize=(8, 5))
plt.bar(top_products['product'].head(5), top_products['quantity'].head(5), color='skyblue')
plt.title('Top 5 Best-Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Chart 2: Simple Line Chart for Sales Trends Over Time
# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['date'])

# Group by date and calculate daily revenue
sales_trend = df.groupby('Date')['Total_Sales'].sum().reset_index()
sales_trend = sales_trend.sort_values('Date')

plt.figure(figsize=(10, 5))
plt.plot(sales_trend['Date'], sales_trend['Total_Sales'], marker='o', color='green')
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

print("\nAnalysis completed successfully!")