from sklearn import datasets
import pandas as pd
date = datasets.load_breast_cancer()
print(type(date))
print(date.keys())
dataframe = pd.DataFrame(date.data,columns=date.feature_names)
print(dataframe)
dataframe["Cancer"] = date.target
print(dataframe)
dataframe.info()

X = dataframe.drop("Cancer",axis=1)
print(X)
y = dataframe["Cancer"]
print(y)