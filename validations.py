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