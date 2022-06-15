import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# 统计电影分类

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

# 统计电影分类类别与个数
genre_list_all = df["Genre"].str.split(",").to_list()  # [[],[],[]]
genre_list = list(set([i for j in genre_list_all for i in j]))
# print(genre_list_all[:3])
# print("*" * 100)
# print(set(genre_list))
# print(len(set(genre_list)))

# 构造全0数组
zero_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))),
                       columns=genre_list)
# print(zero_df)

# 给每个电影分类出现的次数赋值为1
for i in range(df.shape[0]):
    # zero_df.loc[0, genre_list_all[0]]
    # zero_df.loc[0, ['Action', 'Adventure', 'Sci-Fi']]
    zero_df.loc[i, genre_list_all[i]] = 1

# print(zero_df.head(3))

# 统计每个电影分类的数量
genre_sum = zero_df.sum(axis=0)
# print(genre_sum)
# print(type(genre_sum))
genre_sum = genre_sum.sort_values()
print(genre_sum)

# 统计每个电影分类的数量 方法2 直接简单
# genre_count = pd.value_counts([i for j in genre_list_all for i in j])
# print(genre_count, type(genre_count))

plt.figure(figsize=(20, 8), dpi=80)
_x = genre_sum.index
_y = genre_sum.values
plt.bar(_x, _y, color="#8076a3")
plt.show()