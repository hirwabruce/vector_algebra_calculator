from operations import add, subtract, dot_product
from operations import np

print("Welcome to the Vector Algebra Calculator!")
a = np.array([float(x) for x in input("Enter the first vector (comma-separated values): ").split(',')])
b = np.array([float(x) for x in input("Enter the second vector (comma-separated values): ").split(',')])
addition= add(a,b)
print("The result of adding the vectors is:", addition)
subtraction = subtract(a,b)
print("The result of subtracting the vectors is:", subtraction)
dot_product_result = dot_product(a,b)
print("The result of the dot product of the vectors is:", dot_product_result)