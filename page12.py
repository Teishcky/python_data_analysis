import numpy as np

a = np.arange(10)
b = a
c = a.copy()

a[5] = 0

print(a)
print(b)
print(c)