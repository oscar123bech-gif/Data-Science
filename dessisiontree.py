import pandas as pd

csv = pd.read_csv("car.csv")


print(csv["doors"].value_counts())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

csv["sales"] = le.fit_transform(csv["sales"])
csv["maintainance"] = le.fit_transform(csv["maintainance"])
csv["doors"] = le.fit_transform(csv["doors"])
csv["persons"] = le.fit_transform(csv["persons"])
csv["boot_space"] = le.fit_transform(csv["boot_space"])
csv["safety"] = le.fit_transform(csv["safety"])
csv["class"] = le.fit_transform(csv["class"])
csv.info()

X = csv[["sales","maintainance","doors","persons","boot_space","safety"]]
y = csv["class"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.1)

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