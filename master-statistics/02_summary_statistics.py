# Make sure to run this from the root directory of this project.

import numpy as np
import pandas as pd
from scipy import stats
from collections import Counter

cars = pd.read_csv('master-statistics/cars.csv')

# All these are from 01_variables_types.py to clean up the data
print(cars.head())
cars['Weight'] = cars['Weight'].replace(['missing'], np.nan)
cars['Weight'] = cars['Weight'].astype('float')
cars['Rating'] = pd.Categorical(
    cars['Rating'], ['Bad', 'Good', 'Excellent'], ordered=True)
cars['Rating_codes'] = cars['Rating'].cat.codes
cars = pd.get_dummies(data=cars, columns=['Average Education'])

print(cars.info())
print(cars.head())

print(cars.iloc[3:5])  # print rows 3 to 4

print('length', len(cars))


# Mean

print(cars['CO2'].mean())
# print(np.average(['CO2'])) # Doesn't seem to work for some reason
example_array = np.array([24, 16, 30, 10, 12, 28, 38, 2, 4, 36])
example_average = np.average(example_array)  # can also use np.mean
print('mean', example_average)

# Median

print(cars['CO2'].median())
# print(np.median(['CO2']))  # Doesn't seem to work for some reason
example_array = np.array([24, 16, 30, 10, 12, 28, 38, 2, 4, 36, 42])
example_median = np.median(example_array)
print('median', example_median)

# Mode

example_array = np.array([24, 16, 12, 10, 12, 28, 38, 12, 28, 24])
example_mode = stats.mode(example_array)
print(example_mode)
print('The mode is ' + str(example_mode[0][0]) + ' and it appears ' + str(
    example_mode[1][0]) + ' times out of ' + str(len(example_array)))

# Frequency of every unique value

counters = Counter(example_array)
print(counters, counters.items())


# Variance
# Variance = square all the differnces from the mean, then dividie by count
dataset = [3, 5, -2, 49, 10]
variance = np.var(dataset)

# Standard Deviation
# Standard deviation is the square root of the variance.
standard_deviation_of_variance = variance ** 0.5
dataset = [4, 8, 15, 16, 23, 42]
standard_deviation = np.std(dataset)

# Filter
fiats = cars.loc[cars['Car'] == 'Fiat']
print(fiats.head())
