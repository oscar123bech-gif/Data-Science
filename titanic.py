import pandas as pd
csv = pd.read_csv("titanic.csv")
print(csv)
print(csv.head(5))
print(csv.info())
print(csv[["Name","Age"]].head(5))
print(csv)
old = csv[csv["Age"]> 35]
print(old) 
poor = csv[(csv["Pclass"] == 2) | (csv["Pclass"] == 3)]
print(poor)
