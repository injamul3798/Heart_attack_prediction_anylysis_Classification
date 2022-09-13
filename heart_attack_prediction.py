# -*- coding: utf-8 -*-
"""Heart attack Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NIE06J8KTLRtgYAYL6fw_l9DVKDZP1rT

Importing Library and dataset
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/drive/MyDrive/Injam_ML_practice/Heart attack prediction/heart.csv")

df.head()

df.shape

df.isnull().sum().sort_values(ascending=False)

"""Selecting Target and feature values"""

x = df.iloc[:,:-1].values
y = df.iloc[:,-1]

x

y

"""Test_train_split"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)

x_train

y_train

"""**Fitting Model**

Random forest Classifier
"""

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators= 10, criterion="entropy")
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)

y_pred

"""Discussion about accuracy and model"""

from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))

classifier.score(x_test,y_test)

"""Naive Bayes"""

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x_train, y_train)

y_pred = gnb.predict(x_test)

from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,y_pred))

gnb.score(x_test,y_test)

"""Logistic Regression"""

from sklearn.linear_model import LogisticRegression
#Now create object of LogisticRegression
logisModel = LogisticRegression()
#And now fit the model into x_train and y_train
logisModel.fit(x_train,y_train)

y_pred = logisModel.predict(x_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

print(confusion_matrix(y_test,y_pred))

logisModel.score(x_test,y_test)

"""K nearest Neigbour"""

from sklearn.neighbors import KNeighborsClassifier 
classifi = KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2) 
classifi.fit(x_train,y_train)

from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,y_pred))

classifi.score(x_test,y_test)