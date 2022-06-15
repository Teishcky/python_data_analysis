import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SIMYOU.TTF")

data = pd.read_excel('F:\Python_programe\图形绘制\data.xlsx')

plt.figure(figsize=(22, 10), dpi=80)

_x = data['电影名称'].values
y = data['总票房'].values

x = range(len(_x))
# 绘制条形图
plt.bar(x, y, width=0.3)
plt.xticks(x, _x, fontproperties=my_font, rotation=35)

# 也可直接传入 _x
# plt.bar(_x, y, width=0.3)
# plt.xticks(_x, fontproperties=my_font, rotation=35)

# plt.xlabel("电影名称", fontproperties=my_font)
# plt.ylabel("总票房", fontproperties=my_font)
# plt.title("电影票券一览图", fontproperties=my_font)

plt.show()
