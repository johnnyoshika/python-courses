# https://www.w3schools.com/python/python_ml_train_test.asp

import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# Display the training set

plt.scatter(train_x, train_y)
plt.show()

# Display the testing set

plt.scatter(test_x, test_y)
plt.show()

# Based on the plots, polynomial regression looks to be the best

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# Check the r2 score

r2 = r2_score(train_y, mymodel(train_x))

print('r2', r2)  # R2 of 0.8 shows that the model fits the testing set well


# Now predict based on the model

print(mymodel(5))
