import pandas as pd

file_path = './starbucks_store_worldwide.csv'

df = pd.read_csv(file_path)

# 将输出内容显示完全
pd.set_option('display.max_columns', None)

# print(df.head(1))
# print(df.info())

# 1--统计美国和中国的星巴克门店数量
# group1 = df.groupby(by="Country")
# # 1)遍历
# # for i,j in group1:
# #     print(i)
# #     print("-" * 66)
# #     print(j)
# #     print("*" * 66)
# #     break
# # 2)聚合
# country_num = group1["Brand"].count()
# print(country_num["US"])
# print(country_num["CN"])

# 2--统计中国每个省份的星巴克门店数量
# cn_data = df[df["Country"] == "CN"]
# group2 = cn_data.groupby(by="State/Province")
# print(group2["Brand"].count())

# 3--按照多个条件进行分组
group3 = df[["Brand"
             ]].groupby(by=[df["Country"], df["State/Province"]]).count()
# print(group3)
# print(type(group3))
print(group3.index)