import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Salary_Data.csv")

X = dataset.iloc[:,:-1].values    #IMPORTANT- In this case, .iloc[:,0] gives an error(even though there's only one column to be extracted) because :-1 interprets it as a 2-d array with only one column, but ,0 interprets it as a 1-d array. .fit() method requires the former, hence an 'inconsistent sample size' error thrown for the latter
y = dataset.iloc[:,1].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =(1/3), random_state = 0)

#fitting the model to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)


#predicting the values for the test-set by the model thus trained
y_pred = regressor.predict(X_test) #y_pred is a vector of predictions for the feature values in X_test over the model trained above


#plotting the data

plt.close('all')

#Plotting the training set and the regression line
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title("Salary vs Years of Experience(Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


#plotting the test data
plt.figure()
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # same as before because the regression line is the same as the model is already trained
plt.title('Salary vs Years of Experience(Test Set)')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

