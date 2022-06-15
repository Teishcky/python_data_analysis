import numpy as np


# 替换数组中的nan为该列平均值
def fill_ndarray_nan(t):
    for i in range(t.shape[1]):
        data = t[:, i]
        # print(data)
        nan_num = np.count_nonzero(np.isnan(t))
        if nan_num != 0:
            no_nan = data[data == data]
            data[data != data] = no_nan.mean()
        # print(data)
    return t


if __name__ == '__main__':
    t = np.arange(12, dtype=float).reshape((3, 4))

    t[1, 2:] = np.nan

    print(t)
    print("*" * 55)

    t = fill_ndarray_nan(t)
    print(t)
