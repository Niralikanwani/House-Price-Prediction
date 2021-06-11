# using Decission tree
import pandas as pd
import numpy as np
from sklearn import preprocessing

train_df = pd.read_csv('train1.csv')
model_columns = list(train_df.columns)
model_columns = model_columns[:-1]
print(model_columns)

dataset1=train_df.values
X =dataset1[:,0:10]
Y = dataset1[:,10]

print(train_df.describe())

from sklearn.model_selection import train_test_split

X_train,X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.3)
print(X_train.shape, X_test.shape)


print(X_train[0,:])
print(Y_train[0])

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train,Y_train)
score = reg.score(X_test,Y_test)
y_pred = reg.predict(X_test)


# Model prediction
print(score*100)
from sklearn import ensemble
clf = ensemble.GradientBoostingRegressor(n_estimators = 400, max_depth = 5, min_samples_split = 2,
          learning_rate = 0.1, loss = 'ls')

clf.fit(X_train, Y_train)
print(clf.score(X_test,Y_test)*100)

from sklearn.externals import joblib
joblib.dump(clf, 'house_price_res.pickle')
print("Model dumped!")

# Load the model that you just saved
clf = joblib.load('house_price_res.pickle')
# Saving the data columns from training
joblib.dump(model_columns, 'house_price_res_columns.pickle')
print("Models columns dumped!")

