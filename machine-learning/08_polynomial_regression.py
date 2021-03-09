# https://www.w3schools.com/python/python_ml_polynomial_regression.asp

import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# R-squared -> 0 means no relationship 1 meand 100% relationship
print(r2_score(y, mymodel(x)))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# Predict speed of a car passing at 17:00

speed = mymodel(17)
print(speed)