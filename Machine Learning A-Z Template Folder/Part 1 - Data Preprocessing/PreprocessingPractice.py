import numpy as np
import pandas as pd
import matplotlib.pyplot as mlt
import os

#os.chdir(...)
dataset = pd.read_csv("Data.csv")

#splitting the dataset into the feature matrix and the dependent variable vector
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#conpensating for the missing values, if any
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[:,(1,2)])
X[:,(1,2)] = imputer.transform(X[:,(1,2)])


#encoding the categorical features into numerical values
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#compensating for the numertical disparity betweeen the newly assigned numerical labels(only for model where the disparity is not a requisite), by creating dummy, binary features
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

#splitting the dataset into training and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.2) #not providing a seed(for random sampling each time)


#scaling the features
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


#scaling y only for regresiion problems
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)
y_test = sc_y.transform(y_test)

