import pandas as pd

df = pd.read_csv("data/retail_sales.csv")

df["revenue"] = df["quantity"] * df["price"]

print("Total Revenue:", df["revenue"].sum())
print("Top Products:")
print(df.groupby("product")["revenue"].sum().sort_values(ascending=False))
