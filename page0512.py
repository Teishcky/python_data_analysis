import pandas as pd

t1 = pd.Series([12, 23, 342], index=list("abc"))

print(t1)
print("*" * 55)

# temp_dict = {"name": "dzj", "age": 30, "tel": 10086}
temp_dict = {"name": ["dzj", "feifei"], "age": [25, 22], "tel": [10086, 10000]}
t2 = pd.Series(temp_dict)
print(t2)
print("*" * 55)

t3 = pd.DataFrame(temp_dict)
print(t3)
print("*" * 55)
