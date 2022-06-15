from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SIMYOU.TTF")

plt.figure(figsize=(20, 8), dpi=80)

_x = [
    '长津湖', '战狼2', '哪吒之魔童降世', '流浪地球', '复仇者联盟4：终局之战', '红海行动', '美人鱼', '唐人街探案2',
    '我和我的祖国', '我不是药神', '中国机长', '速度与激情8', '西虹市首富', '速度与激情7', '捉妖记',
    '复仇者联盟3：无限战争', '捉妖记2', '羞羞的铁拳', '疯狂的外星人', '海王'
]
y = [1, 2, 3, 3, 3, 5, 7, 7, 10, 10, 13.15, 15, 16, 17, 17, 18, 20, 20, 22, 54]
y.reverse()

x = range(len(_x))
# 绘制横着的条形图
plt.barh(x, y, height=0.5, color="orange")
plt.yticks(x, _x, fontproperties=my_font)

plt.grid(alpha=0.3)

plt.show()
