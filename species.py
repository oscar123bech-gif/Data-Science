import pandas as pd
data = pd.read_csv("iris.csv")
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print (data) 
data["species"] = data["species"].replace({"setosa":1, "versicolor":2,"virginica":3}) 
print(data)


x = data.iloc[:,0:4]
y = data.iloc[:,4:5]
print(x)
print(y)

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=1)
print(xtrain,xtest,ytrain,ytest)

a = DecisionTreeClassifier(max_depth=3,random_state=1)
a.fit(xtrain,ytrain)
predictionresult = a.predict(xtest)
print (predictionresult,ytest)
