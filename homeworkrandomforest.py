import pandas as pd

csv = pd.read_csv("adult.csv")

csv.info()

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

csv["occupation"] = le.fit_transform(csv["occupation"])

csv["race"] = le.fit_transform(csv["race"])

csv["income"] = le.fit_transform(csv["income"])

X = csv[["age","race","occupation"]]

y = csv["income"]

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.1)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train,y_train)

predictedy = rfc.predict(X_test)
print(predictedy)

from sklearn.metrics import confusion_matrix,classification_report
error = confusion_matrix(y_test,predictedy)
print(error)

print(classification_report(y_test,predictedy))
from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()

dtc.fit(X_train,y_train)

predictedy = dtc.predict(X_test)

from sklearn.metrics import confusion_matrix,classification_report
error = confusion_matrix(y_test,predictedy)
print(error)


import matplotlib.pyplot as plt

import seaborn as sns 
sns.heatmap(error,annot=True,fmt="d")

plt.show()
print(classification_report(y_test,predictedy))