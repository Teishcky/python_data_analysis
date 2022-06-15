import page14 as ff
import numpy as np

a = np.arange(24, dtype=float).reshape(3, 8)

a[2, 2] = np.nan
a[0, 5] = np.nan
print(a)

a = ff.fill_ndarray_nan(a)
print(a)