import pandas as pd

df = pd.read_csv("titanic.csv")

df.columns = df.columns.str.strip()

result1 = df[(df['Age'] >= 20) & (df['Age'] <= 40)][['Name', 'Fare']]
print(result1)
print("\n")

result2 = df[df['Fare'] > 100][['Name', 'Pclass']]
print(result2)
print("\n")

result3 = df[(df['Survived'] == 1) & (df['Pclass'] == 3)][['Name']]
print(result3)