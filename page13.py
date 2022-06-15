import numpy as np

t1 = np.arange(24, dtype=float).reshape(4, 6)

# t1[:, 0] = 0

t1[3, 3] = np.nan
print(t1)
print(np.isnan(t1))
t1[np.isnan(t1)] = 0

print(t1)
# print(np.count_nonzero(t1))
# print(np.count_nonzero(t1 != t1))
# print(np.count_nonzero(np.isnan(t1)))
# print(np.sum(t1, axis=1))
