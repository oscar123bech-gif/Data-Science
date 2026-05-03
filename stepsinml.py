import numpy as np
import pandas as pd
data = pd.read_csv("Data.csv")
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

x = data.iloc[ : ,0:3]
y = data.iloc[ : ,3]



imputer = SimpleImputer(missing_values= np.nan,strategy= "mean" )



imputer.fit (x.iloc[ : ,1:3])
x.iloc[ : ,1:3] = imputer.transform(x.iloc[ : ,1:3])
print (x)
print(y)

firstcollum = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])])
x = np.array(firstcollum.fit_transform(x))

print(x)