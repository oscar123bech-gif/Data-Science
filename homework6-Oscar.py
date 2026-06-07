import numpy as np
import pandas as pd
data = pd.read_csv("titanic.csv")

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = data.drop(["Name"], axis=1)

x = data.iloc[:,2:]
y = data.iloc[:,1]

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")

imputer.fit(x.iloc[:,[2,3,4,5,6]])
x.iloc[:,[2,3,4,5,6]] = imputer.transform(x.iloc[:,[2,3,4,5,6]])

print(x)
print(y)

firstcollum = ColumnTransformer(
    transformers=[("encoder",OneHotEncoder(),[1])],
    remainder='passthrough'
)

x = np.array(firstcollum.fit_transform(x))

print(x)

labelencoder = LabelEncoder()
y = labelencoder.fit_transform(y)

print(y)

xtrain,xtest,ytrain,ytest = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=1
)

standard = StandardScaler()

xtrain[:,2:] = standard.fit_transform(xtrain[:,2:])
xtest[:,2:] = standard.transform(xtest[:,2:])

print(xtrain)
print(xtest)
print(ytrain)
print(ytest)


output needs to be survived or not
rest needs to be input 
collum transformer and label encoder are not needed
