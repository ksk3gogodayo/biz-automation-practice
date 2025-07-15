# where_example.py
import pandas as pd

df = pd.read_csv("orders.csv")

# SQL: SELECT * FROM orders WHERE amount > 1000;
filtered_df = df[df["amount"] > 1000]

print(filtered_df)