import random
import numpy as np

load_data = "F:\Python_programe\\numpy数据处理\data.csv"

t1 = np.loadtxt(load_data, delimiter=",", dtype="int", encoding="utf-8-sig")

# a = []
# a += [random.randint(1, 999) for i in range(24)]

comments_t1 = t1[:, -1]
print(comments_t1)