import sqlite3
import pandas as pd

df = pd.read_csv('../data/processed_ecommerce_data.csv')
conn = sqlite3.connect('../data/ecommerce.db')
df.to_sql('ecommerce', conn, if_exists='replace', index=False)

query1 = """
SELECT Product, SUM(TotalSales) as Revenue, SUM(Quantity) as UnitsSold
FROM ecommerce GROUP BY Product ORDER BY Revenue DESC LIMIT 5;
"""
top_products = pd.read_sql_query(query1, conn)
print("Top Products:\n", top_products)

query2 = """
SELECT Region, COUNT(*) as LowStockCount
FROM ecommerce WHERE LowStock = 'Yes' GROUP BY Region ORDER BY LowStockCount DESC;
"""
low_stock = pd.read_sql_query(query2, conn)
print("Low Stock by Region:\n", low_stock)

conn.close()