import pandas as pd
from matplotlib import pyplot as plt

file_path = './BeijingPM20100101_20151231.csv'

df = pd.read_csv(file_path)
pd.set_option('display.max_columns', None)

# 把数据中分开的年月日时分秒的时间字符串通过PeriodIndex方法转化为pandas的时间类型
period = pd.PeriodIndex(year=df["year"],
                        month=df["month"],
                        day=df["day"],
                        hour=df["hour"],
                        freq="H")
df["date"] = period

df.set_index("date", inplace=True)

df = df.resample("7D").mean()

data = df["PM_US Post"]
data_CN = df["PM_Dongsi"]

_x = data.index
_x = [i.strftime("%Y%m%d") for i in _x]
_y = data.values

_x_CN = [i.strftime("%Y%m%d") for i in data_CN.index]
_y_CN = data_CN.values

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x)), _y, label="US")
plt.plot(range(len(_x_CN)), _y_CN, label="CN")

plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)

plt.legend()

plt.show()