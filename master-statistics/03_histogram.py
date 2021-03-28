import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# If we're working with a CSV, we can import it and then isolate exercise_ages in an array
# df = pd.read_csv('master-statistics/exercise_ages.csv')

# # Shows first 5 and last 5 rows
# print(df)

# # Save exercise_ages in a separate numpy array
# exercise_ages = df['Exercise Age'].values

exercise_ages = np.array([22, 27, 45, 62, 34, 52, 42,
                          22, 34, 26, 24, 65, 34, 25, 45, 23, 45, 33, 52, 55])

print('min', np.amin(exercise_ages))
print('max', np.amax(exercise_ages))

# Output is: (array([7, 4, 4, 3, 2]), array([20., 30., 40., 50., 60., 70.]))
# Or, (counts for each bin, min/max values for each bins)
print(np.histogram(exercise_ages, range=(20, 70), bins=5))

plt.hist(exercise_ages, range=(20, 70), bins=5, edgecolor='black')

plt.title("Decade Frequency")
plt.xlabel("Ages")
plt.ylabel("Count")

plt.show()

# ------------------------------------------------------------
# To show multiple plots at once, one above the other, do this:
# ------------------------------------------------------------

# See 03c_quartiles_quantiles_iqr.py for a better example. This one here overlaps each other.

# plt.figure(1)
# plt.subplot(211)

# # Plot flights
# plt.hist(flights, range=(0, 365), bins=365)
# plt.ylabel("Flight Count")

# # Plot bloom
# plt.subplot(212)
# plt.hist(in_bloom, range=(0, 365), bins=365)
# plt.title("Flower Blooms and Flights by Day")
# plt.ylabel("Bloom Count")
# plt.xlabel("Day of the Year")

# plt.show()

# ------------------------------------------------------------
# If you want to plot 2 histograms on top of each other:
# ------------------------------------------------------------

# plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
# plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
# plt.legend()
# plt.show()
