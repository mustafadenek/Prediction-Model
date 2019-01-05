#import libraries
import pandas as pd
import numpy as np

#read the file
data = pd.read_csv('odev_tenis.csv')

#convert categoric values --> numeric
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    # convert weather conditions to numeric values
WindyPlay = data.iloc[:,3:].apply(LabelEncoder().fit_transform) 
    # convert outlook  to numeric values
outlook = data.iloc[:,:1]
ohe = OneHotEncoder(categorical_features = 'all')
outlook = ohe.fit_transform(outlook).toarray()
weather = pd.DataFrame(data = outlook, index = range(14), columns = ['rainy', 'overcast', 'sunny'])

#concatenate the tables: WindyPlay, weather and rest.
LabeledData  = pd.concat([weather, data.iloc[:,1:3], WindyPlay], axis = 1)

#split the data as train & test data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(LabeledData.iloc[:,:-1], LabeledData.iloc[:,-1:], test_size = 0.33, random_state = 0)

#apply a regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

#check the P-value of the model
import statsmodels.formula.api as sm
#X = np.append(arr = np.ones((14,1)).astype(int), values=LabeledData.iloc[:,:-1], axis=1 )
x_1 =LabeledData.iloc[:,[0,1,2,3,4,5]].values
r_ols = sm.OLS(endog = LabeledData.iloc[:,-1:], exog = x_1)
r = r_ols.fit()
print(r.summary())

#start backwardelemination to improve the model...
    #delete the variable having the biggest P-value. and run the fit model again.
x_1 = x_1 =LabeledData.iloc[:,[0,1,2,4,5]].values
r_ols = sm.OLS(endog = LabeledData.iloc[:,-1:], exog = x_1)
r = r_ols.fit()
print(r.summary())

    #delete the variable having the biggest P-value. and run the fit model again.
x_1 = x_1 =LabeledData.iloc[:,[0,1,2,5]].values
r_ols = sm.OLS(endog = LabeledData.iloc[:,-1:], exog = x_1)
r = r_ols.fit()
print(r.summary())
    
    #delete the variable having the biggest P-value. and run the fit model again.
x_1 = x_1 =LabeledData.iloc[:,[0,1,2]].values
r_ols = sm.OLS(endog = LabeledData.iloc[:,-1:], exog = x_1)
r = r_ols.fit()
print(r.summary())

#update the train & test tables after backwardelemination
x_train = x_train.iloc[:,:3]
x_test = x_test.iloc[:, :3]

# fit the new model & run
regressor.fit(x_train, y_train)
predict_play = regressor.predict(x_test)
