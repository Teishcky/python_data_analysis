import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
# print(df.info())

#电影时长的分布情况
runtime_list = df["Runtime (Minutes)"].values
# print(runtime_list)

max_runtime = runtime_list.max()
min_runtime = runtime_list.min()
num_bin = (max_runtime - min_runtime) // 5

# plt.figure(figsize=(20, 8), dpi=80)

# plt.hist(runtime_list, num_bin)

# plt.xticks(range(min_runtime, max_runtime + 5, 5))

# plt.show()

#电影评分的分布情况
rating_list = df["Rating"].values

max_rating = rating_list.max()
min_rating = rating_list.min()

plt.figure(figsize=(20, 8), dpi=80)
plt.hist(rating_list, np.arange(1, 10, 0.5))
plt.xticks(np.arange(1, 10, 0.5))
plt.show()
