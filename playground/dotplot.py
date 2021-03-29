import numpy as np
from matplotlib import pyplot as plt

# Dot plots are pretty cool and appeared many times in 'Mastering Statistics with Python' Codeacademy course.
# It's really just a histogram for small data points and this is how you generate it.

# Source: https://stackoverflow.com/a/64943404/188740

# Create random data
rng = np.random.default_rng(1)  # random number generator
data = rng.integers(0, 21, size=100)
values, counts = np.unique(data, return_counts=True)

# Set formatting parameters based on data
data_range = max(values)-min(values)
width = data_range/2 if data_range < 30 else 15
height = max(counts)/3 if data_range < 50 else max(counts)/4
marker_size = 10 if data_range < 50 else np.ceil(30/(data_range//10))

# Create dot plot with appropriate format
fig, ax = plt.subplots(figsize=(width, height))
for value, count in zip(values, counts):
    ax.plot([value]*count, list(range(count)), marker='o', color='tab:blue',
            ms=marker_size, linestyle='')
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.yaxis.set_visible(False)
ax.set_ylim(-1, max(counts))
ax.set_xticks(range(min(values), max(values)+1))
ax.tick_params(axis='x', length=0, pad=10)

plt.show()
