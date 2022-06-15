import numpy as np
import random

# 三种定义数组的方式 np.array([1,2,...])、np.array(range[5])、np.arrange(10)
# a = np.array([1, 2, 3])
# print(a, type(a))

# b = np.array(range(10))
# print(b, type(b))

# c = np.arange(10, 20, 3)
# print(c.dtype)

# print("*" * 100)

# 设置数组内的数值类型 dtype
# d = np.array(range(5), dtype="float32")
# print(d, d.dtype)

# e = np.array([1, 1, 0, 0, 1], dtype=bool)
# print(e, e.dtype)

# 转换数组内的数值类型 astype
# ee = e.astype("int8")
# print(ee, ee.dtype)

t1 = random.random()
print(t1)
# np.round(x,2) 修改浮点型小数的位数
print(np.round(t1, 3))
