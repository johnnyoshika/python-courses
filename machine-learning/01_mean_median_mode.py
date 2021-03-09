import numpy
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

print('mean', numpy.mean(speed))

print('median', numpy.median(speed))

# number that appears the most (86, 3 times)
# ModeResult(mode=array([86]), count=array([3]))
print('mode', stats.mode(speed))
