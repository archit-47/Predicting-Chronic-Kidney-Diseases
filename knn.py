import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df=pd.read_csv('labelencoded.csv')
df.drop(["rbc","rbcc","wbcc"],axis=1,inplace=True)

x=df.drop('class',axis=1)
y=df['class']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=13)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

y_pred=classifier.predict(x_test)
print(y_pred)

accuracy=accuracy_score(y_test,y_pred)*100
print(accuracy)