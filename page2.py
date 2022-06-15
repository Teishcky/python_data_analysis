import random
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SIMYOU.TTF")

y_3 = [random.randint(1, 15) for i in range(31)]
y_10 = [random.randint(15, 30) for i in range(31)]

x_3 = range(1, 32)
x_10 = range(51, 82)

plt.figure(figsize=(20, 8), dpi=80)

# 绘制散点图
plt.scatter(x_3, y_3, label="3月份")
plt.scatter(x_10, y_10, label="10月份")

plt.legend(prop=my_font)

_x = list(x_3) + list(x_10)
_xticks_labels = ["3月{}日".format(i) for i in x_3]
_xticks_labels += ["10月{}日".format(i) for i in x_3]
plt.xticks(_x[::2], _xticks_labels[::2], fontproperties=my_font, rotation=45)

plt.show()