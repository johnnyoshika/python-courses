import matplotlib.pyplot as plt
from scipy import stats

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

# r = relationship. 0 = no relationship, 1 (and -1) = 100% related
print('r (i.e. relationship)', r)


def mymodel(x): return (slope * x + intercept)


model = list(map(mymodel, x))

plt.scatter(x, y)
plt.plot(x, model)
plt.show()

# r is -0.76 -> not great, but not bad. Let's use this to predict 10 year old car

print('predict 10 year old car', mymodel(10))
