import pandas as pd

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
print(df.info())
# rating_mean = df["Rating"].mean()
# print(rating_mean)

# print(len(set(df["Director"].tolist())))
# print(len(df["Director"].unique()))

print(df.head())

# print(t["Actors"])
# print("*" * 66)
# print(t["Actors"].str.split(", ").tolist())

kk = df["Actors"].str.split(", ").tolist()
actors = [i for j in kk for i in j]

print(len(set(actors)))

max_time = df["Runtime (Minutes)"].max()
max_time_index = df["Runtime (Minutes)"].argmax()

print(max_time, max_time_index, df.loc[828, "Title"])
