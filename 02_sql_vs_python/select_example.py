# select_example.py

import pandas as pd

# CSVファイル読み込み
df = pd.read_csv("../01_sql_practice/data/orders.csv")

# SQLでいう「SELECT customer_name, product FROM orders」
result = df[["customer_name", "product"]]

# 結果表示
print(result)