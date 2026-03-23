import pandas as pd

csv = pd.read_csv("titanic.csv")

print(csv)
print(csv.head(5))
print(csv.info())
print(csv[["Name","Age"]].head(5))


old = csv[csv["Age"] > 35]
print(old)


poor = csv[(csv["Pclass"] == 2) | (csv["Pclass"] == 3)]
print(poor)


female_firstclass_old = csv[(csv["Sex"] == "female") &(csv["Pclass"] == 1) &(csv["Age"] > 50)]

print("Female, Pclass=1, Age>50:")
print(female_firstclass_old.head(5))


children_under12_thirdclass = csv[(csv["Age"] < 12) &(csv["Pclass"] == 3)]

print("Children (<12) and in Pclass 3:")
print(children_under12_thirdclass.head(5))

male_class1 = csv[(csv["Sex"] == "male") & (csv["Pclass"] == 1 )]
print(male_class1.head(5))

print(male_class1["Fare"].mean())


female_class2 = csv[(csv["Sex"] == "female") & (csv["Pclass"] == 2 )]
print(female_class2["Fare"].mean())

drinkingage = csv[csv["Age"] > 18]
print(drinkingage["Name"].head(5))

name = csv.loc[csv["Age"] > 18,"Name"]
print(name.head(5))
print(csv.iloc[6:11,2:])
# csv.iloc[16:26,7] = 20
# print(csv.iloc[16:26,7])
csv.to_csv("titanic.csv")
csv["NewFare"] = csv["Fare"] *2
csv.to_csv("titanic.csv")

print(csv["Age"].mean())
print(csv.agg({
    "Age": ["min","max","mean"]
}))