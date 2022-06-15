import random
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SIMYOU.TTF")

# x = [random.randint(90, 100) for i in range(20)]

x = [
    91, 100, 94, 92, 94, 95, 93, 95, 95, 90, 96, 100, 100, 99, 92, 90, 96, 90,
    97, 93
]

d = 5

# 绘制直方图(数据是没有进行过统计的数据)
plt.hist(x, d)

plt.grid()

plt.show()