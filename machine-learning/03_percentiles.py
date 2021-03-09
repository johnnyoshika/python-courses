# https://www.w3schools.com/python/python_ml_percentile.asp

import numpy

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39,
        80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

print('75 percentile', numpy.percentile(ages, 75))
