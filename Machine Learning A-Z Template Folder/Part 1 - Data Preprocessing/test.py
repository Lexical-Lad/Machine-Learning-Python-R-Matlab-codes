import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading the dataset into a pandas dataframe
dataset = pd.read_csv("Data.csv")

#splitting into feature matrix and dependent variable vector
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#using Imputer class to compensate for the missing feature values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy= 'mean', axis = 0)
imputer = imputer.fit(X[:,(1,2)])
X[:,1:3] = imputer.transform(X[:,1:3])

from sklearn.preprocessing import LabelEncoder,OneHotEncoder

#encoding the categorical features into numerical values
labelencoder_X= LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
labelencoder_y = LabelEncoder()
y[:] = labelencoder_y.fit_transform(y[:])   # or y =  labelencoder_y.fit_transform(y), as y is a vector

#using the categorical features thus converted to numerical labels to create dummy columns with 0/1(binary) values to eliminate the relative numerical disparity between them
#This step is only required for categorical feature columns and not the dependent variable vector as its value sain't used for defining the mathematical model
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

#splitting the dataset into training set and test set(80-20 ratio) and using a seed of '0'(for consistency with the course(ignore the explicit seed specification for random sampling every time))
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) #only transform as the object is already fitted to the training set, and test set needs to be transformed on the same basis

#in this particular case, as 'tis just a categorical variable(classification problem), we don't need to apply scaling to the dependent variable(HAS TO BE APPLIED IN CASE OF REGRESSION PROBLEMS)

