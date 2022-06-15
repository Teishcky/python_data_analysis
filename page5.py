from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SIMYOU.TTF")

plt.figure(figsize=(20, 8), dpi=80)

a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛佒：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

barh_width = 0.2
x_14 = list(range(len(a)))
x_15 = [i + barh_width for i in x_14]
x_16 = [i + barh_width for i in x_15]
# 绘制横着的条形图
plt.barh(x_14, b_14, height=barh_width, label="day 14", color="#9932CC")
plt.barh(x_15, b_15, height=barh_width, label="day 15", color="#00FFFF")
plt.barh(x_16, b_16, height=barh_width, label="day 16", color="#F08080")

plt.yticks(x_15, a, fontproperties=my_font)

plt.ylabel("Movie")
plt.legend(prop=my_font)

plt.grid(alpha=0.3)

plt.show()