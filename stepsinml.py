import numpy as np
import pandas as pd
data = pd.read_csv("Data.csv")

x = data.iloc[ : ,0:3]
y = data.iloc[ : ,3]

print (x)
print(y)