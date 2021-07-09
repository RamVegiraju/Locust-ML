import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import pickle

#Read in data
df = pd.read_csv('petrol_consumption.csv')

#Split and prepare data
X = df.drop('Petrol_Consumption', axis = 1)
y = df['Petrol_Consumption']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
sc = StandardScaler()
X_train = sc.fit_transform(X_train) 
X_test = sc.transform(X_test) 

#Model Creation & Prediction
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=30)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test) 

print(int(regressor.predict([[9.0, 3571, 1976, .525]])))

#Error
#print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

#Pickle model for Flask App
pickle.dump(regressor, open('model.pkl', 'wb'))
