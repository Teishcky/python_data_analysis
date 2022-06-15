#!/usr/bin/python3
from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14, 11, 22, 24, 25, 26, 18, 11, 12, 14]

plt.figure(figsize=(20, 8), dpi=80)

# 传入x轴和y轴数据
plt.plot(x, y)

xzhou = [i / 2 for i in range(4, 49)]
# 定义x轴和y轴的步长
plt.xticks(xzhou[::4])
plt.yticks(range(min(y), max(y)))

# 保存图片
# plt.savefig("t1111.svg")

# 展示图片
plt.show()
