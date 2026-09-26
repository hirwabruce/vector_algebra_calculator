from operations import add, subtract, dot_product
from operations import np


def get_vector(message):
    while True:
        user_input = input(message).strip()

        # Check for empty input
        if not user_input:
            print("Error: Please enter at least one number.")
            continue

        try:
            values = [float(x.strip()) for x in user_input.split(",")]

            # Check for empty values, e.g. 2,,5
            if any(x.strip() == "" for x in user_input.split(",")):
                print("Error: Empty value detected. Example: 2,7,5")
                continue

            return np.array(values)

        except ValueError:
            print("Error: Please enter numbers separated by commas.")
            print("Example: 2,7,5 or 2.5,7,5")


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