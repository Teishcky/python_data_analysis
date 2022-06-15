import pandas as pd
from matplotlib import pyplot as plt

file_path = './starbucks_store_worldwide.csv'

df = pd.read_csv(file_path)

data = df.groupby(by="Country").count()["Brand"].sort_values(
    ascending=False)[:10]

_x = data.index
_y = data.values

plt.figure(figsize=(20, 8), dpi=80)

plt.bar(_x, _y)

plt.show()
