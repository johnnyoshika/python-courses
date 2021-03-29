# %% [markdown]
# ## Let's get this party started!!!

# * Line 1
# * Line 2

# %%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

cp_data = pd.read_csv('chest_pain_treatment_costs.csv')
cp_data.head()

# %%
states = cp_data['Provider State'].unique()
datasets = []
for state in states:
    datasets.append(cp_data[cp_data['Provider State'] ==
                            state][' Average Covered Charges '].values)

# Make figure long so that boxplots for all 50 states will fit
plt.figure(figsize=(20, 6))
plt.boxplot(datasets, labels=states)
plt.show()
