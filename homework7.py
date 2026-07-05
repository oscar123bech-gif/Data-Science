import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("housing.csv")


df = df[df['median_house_value'] < 500000]

plt.figure(figsize=(12, 10))


plt.subplot(2, 2, 1)
plt.scatter(df['median_income'], df['median_house_value'])
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("Median Income vs Median House Value")


plt.subplot(2, 2, 2)
plt.hist(df['housing_median_age'])
plt.xlabel("Housing Median Age")
plt.ylabel("Frequency")
plt.title("Housing Median Age Distribution")


plt.subplot(2, 2, 3)
plt.scatter(df['longitude'], df['latitude'], c=df['median_house_value'])
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Longitude vs Latitude (by House Value)")

plt.suptitle("California Housing Data Dashboard", fontsize=16)

plt.tight_layout()
plt.show()
