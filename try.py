import random
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 引入字体
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SIMYOU.TTF")

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

#图像大小和清晰度
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

_xsticks_labels = ["10点{}分".format(i) for i in range(60)]
_xsticks_labels += ["11点{}分".format(i) for i in range(60)]

#x轴刻度设置中文字符串、调整角度、字体
plt.xticks(list(x)[::5],
           _xsticks_labels[::5],
           rotation=45,
           fontproperties=my_font)

#添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("摄氏度", fontproperties=my_font)
plt.title("时间温度表", fontproperties=my_font)

plt.show()