import pandas as pd

file_path = './ceshi.csv'

df = pd.read_csv(file_path)

# print(df)

data = df["分类"].str.split("：").tolist()

print(data)

cate_list = [i[0] for i in data]
# print(cate_list)

# # pp = pd.DataFrame(data, columns=["A", "B"])
# # group_pp = pp.groupby(by="A")
# # print(group_pp.count())

df["cate"] = cate_list
print(df)
print(df.groupby(by="cate").count()["分类"])
