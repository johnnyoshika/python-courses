import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# To describe the distribution of a dataset, you need to describe the following:
# - Center
# - Spread
# - Skew
# - Modality
# - Outliers

# To get this data, I went here: https://data.cms.gov/Medicare-Inpatient/Inpatient-Prospective-Payment-System-IPPS-Provider/97k6-zzx3
# and downloaded their CSV. Opened it in Excel, created a pivot table, found all counts of `DRG Definition` column. I found '313 - CHEST PAIN' in there,
# double clicked it to create a sheet of those records, and exported it to chest_pain_treatment_costs.csv.
cp_data = pd.read_csv('master-statistics/chest_pain_treatment_costs.csv')

# We could have, of course, filtered that data here:
# cp_data = cp_data[cp_data['DRG Definition'] == '313 - CHEST PAIN']

print(cp_data)
print(cp_data.dtypes)

ave_covered_charges = cp_data[' Average Covered Charges ']

# Center

print('average', ave_covered_charges.mean())
print('median', ave_covered_charges.median())

# Spread

print('min', ave_covered_charges.min())
print('max', ave_covered_charges.max())
print('range', ave_covered_charges.max() - ave_covered_charges.min())

# Skew

# This is right skewed, b/c the tail goes far to the right and mean is greater than the median

# Modality

# It's also has a unimodal distribution, as it only has one peak. If it had 2, it would have a bimodal distribution.

# Outlier

# The larges cost is also an outlier, based on the plot befow

plt.hist(ave_covered_charges, range=(0, 80000), bins=100, edgecolor='black')
plt.axvline(x=ave_covered_charges.mean(), label='Average', c='r')
plt.title('Cheat Pain Treatment')
plt.xlabel('Average Coverage charges')
plt.ylabel('Count')
plt.legend()
plt.show()
