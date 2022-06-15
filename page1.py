import random
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SIMYOU.TTF")

x = range(11, 31)
y_1 = [random.randint(1, 6) for i in range(20)]
y_2 = [random.randint(2, 7) for i in range(20)]

plt.figure(figsize=(20, 8), dpi=80)

# 绘制折线图
plt.plot(x, y_1, label="自己", color="#7FFFAA", linestyle=":")
plt.plot(x, y_2, label="同桌", color="cyan", linestyle="--")

_x_stick = ["{}岁".format(i) for i in x]
plt.xticks(x, _x_stick, fontproperties=my_font)
plt.yticks(range(0, 9))

# 绘制网格
plt.grid(alpha=0.4)

# 添加图例
plt.legend(prop=my_font, loc="upper left")

plt.show()