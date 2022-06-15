import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SIMYOU.TTF")

file_path = './starbucks_store_worldwide.csv'

df = pd.read_csv(file_path)
df = df[df["Country"] == "CN"]

data = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:25]

_x = data.index
_y = data.values

plt.figure(figsize=(20, 8), dpi=80)

# plt.bar(_x, _y, width=0.3, color="#621624")
# plt.xticks(fontproperties=my_font)

plt.barh(_x, _y, height=0.4, color="#621624")
plt.yticks(fontproperties=my_font)

plt.show()