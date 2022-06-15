import pandas as pd
from matplotlib import pyplot as plt

file_path = './ceshi.csv'

# 统计数据中不同时间不同分类的分布情况
df = pd.read_csv(file_path)

# df中新增cate一列
cate_list = df["分类"].str.split("：").tolist()
cate_data = [i[0] for i in cate_list]
df["cate"] = cate_data

# 将时间一列的字符串类型数据转换为时间类型，同时设置为索引
df["时间"] = pd.to_datetime(df["时间"])
df.set_index("时间", inplace=True)

plt.figure(figsize=(20, 8), dpi=80)

# 按照分类进行分组，得到（分类，数据）这样的元组结果
group_data = df.groupby(by="cate")
# for i in group_data:
#     print(i)
#     print("-" * 77)

for group_cate, group_dd in group_data:
    count_by_month = group_dd.resample("M").count()["名称"]
    _x = count_by_month.index
    _y = count_by_month.values

    # 时间格式化
    _x = [i.strftime("%Y%m%d") for i in _x]

    plt.plot(range(len(_x)), _y, label=group_cate)

plt.xticks(range(len(_x)), _x)
plt.xlabel("TIME")
plt.ylabel("TIMES")
plt.legend()
plt.show()
