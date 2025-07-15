# 01_sql_practice

SQLの基本構文や集計処理、JOINなどの練習用フォルダです。  
ダミーデータを使って業務イメージをつかみながら記述していきます。

## ✅ やることリスト

- [ ] SELECT / WHERE の書き方確認
- [ ] JOIN で複数テーブル結合
- [ ] GROUP BY / HAVING の集計処理
- [ ] サブクエリ・ウィンドウ関数の基礎

---

📁 データ： `data/` フォルダにCSV入れる予定  
📝 クエリ： `queries.sql` に保存

---

## Pythonでの同様処理（参考）

SQLのJOINやGROUP BY的な処理は、Python（pandas）でも可能です。  
以下のサンプルスクリプトでは、2つのCSVデータを結合し、グループ集計しています。

```python
import pandas as pd

orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

# JOIN（内部結合）
merged = pd.merge(orders, customers, on="customer_id", how="inner")

# GROUP BY（合計）
summary = merged.groupby("customer_name")["amount"].sum().reset_index()

print(summary)

📌 補足：Python（pandas）を用いた同様処理も記載中。SQLに加え、処理自動化やデータ活用の視点からも学習を進めています。
