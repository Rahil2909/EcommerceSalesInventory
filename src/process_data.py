import pandas as pd

df = pd.read_csv('../data/ecommerce_data.csv')
df['TotalSales'] = df['Quantity'] * df['UnitPrice']
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['LowStock'] = df['StockLevel'].apply(lambda x: 'Yes' if x < 5 else 'No')
df.to_csv('../data/processed_ecommerce_data.csv', index=False)
print("Data processed and saved to ../data/processed_ecommerce_data.csv")