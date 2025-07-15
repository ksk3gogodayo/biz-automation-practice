# select_example.py
import pandas as pd

# CSVの読み込み
df = pd.read_csv("../01_sql_practice/data/orders.csv")

# SQL: SELECT customer_name, product FROM orders;
print(df[["customer_name", "product"]])