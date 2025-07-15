# select_example.py

import pandas as pd

df = pd.read_csv("orders.csv")

# SQL: SELECT customer_name, product FROM orders;
print(df[["customer_name", "product"]])
