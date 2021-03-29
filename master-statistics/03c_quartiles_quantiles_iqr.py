import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import iqr

# If you have n quantiles, the dataset will be split into n+1 groups of equal size

# Deciles
# Deciles are a special form of quantiles with 10 groups.

# Percentiles
# Percentiles are a special form of quantiles with 100 groups.

# Quartiles
# Quartiles are a special form of quantiles with 4 groups.

# Quartile 2 is the same as the median

dataset_one = [-20, -3, 2, 4, 4, 10, 50]
dataset_one_q2 = 4

# Quartile 1 is the median of everything to the left of Q2
# Quartile 3 is the median of everything to the right of Q2

dataset_one_q1 = -3
dataset_one_q3 = 10

# Numpy includes the mean when calculating Q1 and Q3,
# and that's why it differs from the numbers above
print('Q1', np.quantile(dataset_one, 0.25))
print('Q2', np.quantile(dataset_one, 0.5))
print('Q3', np.quantile(dataset_one, 0.75))

# Or even easier
print('quartiles', np.quantile(dataset_one, [0.25, 0.5, 0.75]))

# range (shown below) is pretty cool, but only works for integers. For float, use numpy:
print(np.arange(0.1, 1.0, 0.1))
# np.arange(0.1, 1.0, 0.1) is useful for calculating deciles
# np.arange(0.1, 1.0, 0.01) is useful for calculating percentiles

# See 03b_describe_a_histogram.py on how this data was retrieved
cp_data = pd.read_csv('master-statistics/chest_pain_treatment_costs.csv')
ave_covered_charges = cp_data[' Average Covered Charges ']

# Interquartile Range (IQR)
q1 = np.quantile(ave_covered_charges, 0.25)
q3 = np.quantile(ave_covered_charges, 0.75)
interquartile_range = q3 - q1
print('Total range', ave_covered_charges.max() - ave_covered_charges.min())
print('IQR is the range between Q1 and Q3 and gets rid of the outliers',
      interquartile_range)
#   Can also use scipy to calculate IQR
print('IQR with scipy', iqr(ave_covered_charges))
# IQR is often displayed in a box plot

# Quantiles

q1 = np.quantile(ave_covered_charges, 0.25)
q2 = np.quantile(ave_covered_charges, 0.5)
q3 = np.quantile(ave_covered_charges, 0.75)

plt.subplot(3, 1, 1)
plt.hist(ave_covered_charges, bins=200)
plt.axvline(x=q1, c='r')
plt.axvline(x=q2, c='r')
plt.axvline(x=q3, c='r')
plt.xlabel("Cost ($)")
plt.ylabel("Count")
plt.title("4-Quantiles")

plt.subplot(3, 1, 2)
plt.hist(ave_covered_charges, bins=200)
plt.axvline(x=np.quantile(ave_covered_charges, 0.2), c='r')
plt.axvline(x=np.quantile(ave_covered_charges, 0.4), c='r')
plt.axvline(x=np.quantile(ave_covered_charges, 0.6), c='r')
plt.axvline(x=np.quantile(ave_covered_charges, 0.8), c='r')
plt.xlabel("Cost ($)")
plt.ylabel("Count")
plt.title("5-Quantiles")

plt.subplot(3, 1, 3)
plt.hist(ave_covered_charges, bins=200)
for i in range(1, 10):
    plt.axvline(x=np.quantile(ave_covered_charges, i/10), c='r')
plt.xlabel("Cost ($)")
plt.ylabel("Count")
plt.title("10-Quantiles")

plt.tight_layout()
plt.show()
