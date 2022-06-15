import pandas as pd

df = pd.read_csv('./ceshi.csv')
df = df.sort_values(by="数目-number", ascending=False)

print(df["名称-name"])
# print(df[(df["数目-number"] > 5) & (df["名称-name"].str.len() < 4)])
