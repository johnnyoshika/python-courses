import example
import foo

n = [1, 2, 3, 4, 5, 6, 7]

# this returns an iterator, so need to convert to a list
filtered = filter(lambda x: x % 2 == 0, n)
convertToList = list(filtered)
print(convertToList)

print('foo.a', foo.a)
print('foo.b', foo.b)

print(example.add(1, 3))
