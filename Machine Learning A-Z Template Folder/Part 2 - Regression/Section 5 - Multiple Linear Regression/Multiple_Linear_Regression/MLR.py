import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

dataset = pd.read_csv("50_Startups.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()
X[:,3] = labelencoder.fit_transform(X[:,3])

onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()


#Accounting for the Dummy Variable Trap 

X = X[:,1:]

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)


plt.close('all')
plt.figure()
plt.scatter(y_test,y_pred, color = 'red', marker = '.')
plt.xlabel('Actual Profit')
plt.ylabel('Predicted Profit')
plt.plot(y_test, y_test, color = 'blue')
plt.show()
