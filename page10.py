import random
import numpy as np

# load_data = "F:\Python_programe\\numpy数据处理\data.csv"

# t1 = np.loadtxt(load_data, delimiter=",", dtype="int", encoding="utf-8-sig")

a = []
a += [random.randint(1, 999) for i in range(24)]

t = np.array(a).reshape(4, 6)

print(t)

print("-" * 55)
max_data = max(t[range(t.shape[0]), list(np.argmax(t, axis=1))])
min_data = min(t[range(t.shape[0]), list(np.argmin(t, axis=1))])
print(max_data, " ", min_data)
