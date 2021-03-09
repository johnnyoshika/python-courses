# https://www.w3schools.com/python/python_ml_multiple_regression.asp

import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

# Tip: It is common to name the list of independent values with a upper case X, and the list of dependent values with a lower case y.

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)

c = regr.coef_

# if the weight increased by 1kg, the CO2 emission increases by 0.007555g
print('weight coefficient', c[0])
# if the volume increased by 1 cm3, the CO2 emission increases by 0.00780b
print('volume coefficient', c[1])
