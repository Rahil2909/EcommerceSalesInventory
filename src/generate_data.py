import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
n_rows = 10000
dates = [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(n_rows)]
products = np.random.choice(['Laptop', 'Phone', 'Shirt', 'Shoes', 'Chair'], n_rows)
categories = np.random.choice(['Electronics', 'Clothing', 'Furniture'], n_rows)
quantities = np.random.randint(1, 10, n_rows)
unit_prices = np.random.uniform(10, 1000, n_rows).round(2)
regions = np.random.choice(['North', 'South', 'East', 'West'], n_rows)
stock_levels = np.random.randint(0, 50, n_rows)

df = pd.DataFrame({
    'OrderID': range(1, n_rows + 1), 'OrderDate': dates, 'Product': products, 
    'Category': categories, 'Quantity': quantities, 'UnitPrice': unit_prices, 
    'Region': regions, 'StockLevel': stock_levels
})
df.to_csv('../data/ecommerce_data.csv', index=False)
print("Data generated and saved to ../data/ecommerce_data.csv")