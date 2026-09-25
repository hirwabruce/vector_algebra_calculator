from operations import add
from operations import np

print("Welcome to the Vector Algebra Calculator!")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = add(a, b)
print("The result of adding the vectors is:", c)