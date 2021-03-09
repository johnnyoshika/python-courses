# https://www.w3schools.com/python/python_ml_data_distribution.asp

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()
