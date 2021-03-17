# Make sure to run this from the root directory of this project.

import numpy
import pandas

cars = pandas.read_csv('master-statistics/cars.csv')

# Investigate data:
# ------------------------------
# print(cars.head())
# print(cars.tail())
# print(cars.dtypes) # not as useful as cars.info()
# print(cars.info())
# print(cars['Car'].unique())


# Fix Weight column by replacing 'missing' string values with numpy.nan,
# then calculate the mean Weight:
# ------------------------------
# print(cars['Weight'].unique())
cars['Weight'] = cars['Weight'].replace(['missing'], numpy.nan)
# print(cars['Weight'].unique())
cars['Weight'] = cars['Weight'].astype('float')
# print(cars.info())
# print(cars['Weight'].mean())

# Convert 'Rating' to an ordinal category:
# ------------------------------
# print(cars.dtypes)
# print(cars['Rating'].unique())
cars['Rating'] = pandas.Categorical(
    cars['Rating'], ['Bad', 'Good', 'Excellent'], ordered=True)
# print(cars.dtypes)
# print(cars['Rating'].unique())

# Categorical encoding (convert categories into numbers)
# using label encoding
# ------------------------------
cars['Rating_codes'] = cars['Rating'].cat.codes
# print(cars.head())

# Categorical encoding (convert categories into numbers)
# using one-hot encoding
# ------------------------------
# print(cars['Average Education'].unique())
# print(cars.dtypes)
cars = pandas.get_dummies(data=cars, columns=['Average Education'])
# print(cars.head())
# print(cars.dtypes)
