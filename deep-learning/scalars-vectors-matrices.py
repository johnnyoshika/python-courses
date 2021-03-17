import numpy

# Source: https://www.codecademy.com/learn/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/dlsp-introduction-to-deep-learning/cheatsheet

# 0-D tensor
print('scalar', 5)

# 1-D tensor
print('vector', numpy.array([1, 2, 3, 4]))

# 2-D tensor
print('matrix')
print(numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 3-D tensor
print('cube or stack of matrices')
print(numpy.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]))

matrix_addition = numpy.array([[1, 6], [3, 2]]) + numpy.array([[2, 1], [5, 6]])
print('matrix addition', matrix_addition)

scalar_multiplication = 2 * numpy.array([[3, 5], [-2, 12]])
print('scalar_multiplication', scalar_multiplication)

matrix_multiplication = numpy.matmul(numpy.array(
    [[1, 6], [3, 2]]), numpy.array([[2, 1], [5, 6]]))
print('matrix_multiplication', matrix_multiplication)
