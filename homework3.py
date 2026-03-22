import pandas as pd

# create data
data = {
    "Name": ["Tom","Jack","Sam","Leo","Ryan","Alex"],
    "Maths": [80,67,92,74,88,79],
    "Science": [75,70,90,60,85,77],
    "English": [82,65,91,72,80,76]
}

df = pd.DataFrame(data)

print(df)


df["Average"] = 0
df["Average"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Average"] / 3

print("Average Marks:")
print(df)


math_high = df["Maths"].max()
sci_high = df["Science"].max()
eng_high = df["English"].max()

print("Highest Maths:", math_high)
print("Highest Science:", sci_high)
print("Highest English:", eng_high)


result = df[df["Maths"] > 75]

print("Students scoring above 75 in Maths")
print(result)