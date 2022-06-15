import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SIMYOU.TTF")

file_path = './books.csv'

df = pd.read_csv(file_path)

# print(df.head(1).to_string())
# print("-" * 77)
# print(df.info())

# # 统计不同年份出版书籍的数目
# data1 = df[pd.notnull(df["original_publication_year"])]
# group1 = data1.groupby(by="original_publication_year").count()["title"]
# group1 = group1[group1 > 100]

# # print(list(map(str, list(group1.index))))
# # print("-" * 77)
# # print(group1.values)
# # print("-" * 77)
# # print(type(group1), len(group1))

# _x = list(map(str, group1.index))
# _y = group1.values

# plt.figure(figsize=(20, 8), dpi=80)

# plt.bar(_x, _y, width=0.3)

# plt.show()

# 统计不同年份书籍评分情况
data2 = df[pd.notnull(df["original_publication_year"])]
group2 = data2.groupby(by="original_publication_year")["average_rating"].mean()
# print(group2)

_x = group2.index
_y = group2.values

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x)), _y)
plt.xticks(list(range(len(_x)))[::10], _x[::10].astype(int), rotation=45)

plt.show()