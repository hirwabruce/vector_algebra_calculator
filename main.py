from operations import add, subtract, dot_product
from operations import np
from validations import get_vector

print("Welcome to the Vector Algebra Calculator!")

a = get_vector("Enter the first vector (comma-separated values): ")
b = get_vector("Enter the second vector (comma-separated values): ")

# Check vector dimensions
if len(a) != len(b):
    print("\nError: The two vectors must have the same number of elements.")
    print(f"First vector has {len(a)} elements.")
    print(f"Second vector has {len(b)} elements.")
else:
    addition = add(a, b)
    print("The result of adding the vectors is:", addition)

    subtraction = subtract(a, b)
    print("The result of subtracting the vectors is:", subtraction)

    dot_product_result = dot_product(a, b)
    print("The result of the dot product of the vectors is:", dot_product_result)