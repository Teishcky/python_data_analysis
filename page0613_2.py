import pandas as pd
from matplotlib import pyplot as plt

file_path = './ceshi.csv'

df = pd.read_csv(file_path)

# print(type(df["时间"][0]))

df["时间"] = pd.to_datetime(df["时间"])
df.set_index("时间", inplace=True)
print(df)
count_by_10D = df.resample("10D").count()["名称"]
print(count_by_10D)
# print(type(df["时间"][0]))

plt.figure(figsize=(20, 8), dpi=80)

_x = count_by_10D.index
_y = count_by_10D.values
print(_x)
print(_y)
plt.plot(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x)
plt.show()
