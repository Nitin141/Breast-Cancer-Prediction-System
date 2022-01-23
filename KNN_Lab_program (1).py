# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:58:01 2019

@author: bit-cse
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris_dataset=load_iris()

print("\n IRIS FEATURES \ TARGET NAMES: \n ", iris_dataset.target_names)
for i in range(len(iris_dataset.target_names)):
	print("\n[{0}]:[{1}]".format(i,iris_dataset.target_names[i]))

X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)

kn = KNeighborsClassifier(n_neighbors=4)
kn.fit(X_train, y_train)

i=1
x = X_test[i]
x_new = np.array([x])
for i in range(len(X_test)):
    x = X_test[i] 
    x_new = np.array([x])
    prediction = kn.predict(x_new)
    print("\n Actual: {0} {1}, Predicted: {2} {3}".format(y_test[i], iris_dataset.target_names[y_test[i]], prediction, iris_dataset.target_names[prediction]))

print("\n TEST SCORE[ACCURACY]: {:.2f}\n".format(kn.score(X_test, y_test)))

