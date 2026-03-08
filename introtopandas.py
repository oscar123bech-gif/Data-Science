import pandas as pd

df = pd.DataFrame({"name":["oscar","sruthi"],"age":[13,34],"gender": ["Male","Female"]})
print (df)
print(df.head(1))
print (df.shape)
print(df.info())
print(df.describe())
print(df["name"])