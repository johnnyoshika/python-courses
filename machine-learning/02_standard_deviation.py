# https://www.w3schools.com/python/python_ml_standard_deviation.asp

import numpy

speed = [86, 87, 88, 86, 87, 85, 86]

print('std', numpy.std(speed))

# std ^2 == variance

print('variance', numpy.var(speed))
