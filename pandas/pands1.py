import pandas as pd

s = pd.Series([10, 20, 30])
print(s)

data = {
    "name": ["Amit", "Anit", "Akit", "rati", "sati", "mati", "kati"],
    "age": [20, 21, 22, 23, 24, 25, 26]
}
df = pd.DataFrame(data)
# print(df)

dc = pd.read_csv("pandas\e.csv")
# print(dc)

print(df.tail())
print(df.info())
print(df.describe())

print(df.sort_values('name',ascending=False))
print(df)
