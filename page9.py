import numpy as np

# load_data = "F:\Python_programe\\numpy数据处理\data.csv"

# t1 = np.loadtxt(load_data, delimiter=",", dtype="int", encoding="utf-8-sig")

t1 = np.arange(1, 25).reshape(4, 6)
print(t1)

print("*" * 50)

t2 = t1
# t2[t2 < 10] = 3
# t3 = np.where(t2 < 10, 0, 10)
# t3 = t2.clip(10, 18)

t = t1
# t[[1, 2], :] = t[[2, 1], :]
t[:, [2, 3]] = 0
print(t)
