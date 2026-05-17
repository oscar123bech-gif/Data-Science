import pandas as pd
data = pd.read_csv("iris.csv")
print (data) 
data["species"] = data["species"].replace({"setosa":1, "versicolor":2,"virginica":3}) 
print(data)


x = data.iloc[:,0:4]
y = data.iloc[:,4:5]
print(x)
print(y)