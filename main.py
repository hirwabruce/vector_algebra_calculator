from operations import add
from operations import np

print("Welcome to the Vector Algebra Calculator!")
a = np.array([float(x) for x in input("Enter the first vector (comma-separated values): ").split(',')])
b = np.array([float(x) for x in input("Enter the second vector (comma-separated values): ").split(',')])
addition= add(a,b)
print("The result of adding the vectors is:", addition)