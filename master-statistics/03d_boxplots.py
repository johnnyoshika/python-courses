import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# See 03b_describe_a_histogram.py on how this data was retrieved
cp_data = pd.read_csv('master-statistics/chest_pain_treatment_costs.csv')

# There are many different ways to plot the whiskers of a boxplot.
# However, one of the most commonly used methods is to extend them 1.5 times the interquartile range from the first and third quartile.
# For example, if the IQR is 5, the whiskers would extend up to 7.5 below Q1 (where the last point lies) and up to 7.5 above Q3 (where the last point lies).

# Just for testing, plot alabama costs
# alabama_chest_pain = cp_data[cp_data['Provider State'] == 'AL']
# costs = alabama_chest_pain[' Average Covered Charges '].values

states = cp_data['Provider State'].unique()
datasets = []
for state in states:
    datasets.append(cp_data[cp_data['Provider State'] ==
                            state][' Average Covered Charges '].values)

# Make figure long so that boxplots for all 50 states will fit
plt.figure(figsize=(20, 6))
plt.boxplot(datasets, labels=states)
plt.show()

dataset_one = [1, 2, 3, 4, 5]
dataset_two = [3, 4, 5, 6, 7]
plt.boxplot([dataset_one, dataset_two], labels=[
            "Dataset 2", "Dataset 3"])
plt.show()
