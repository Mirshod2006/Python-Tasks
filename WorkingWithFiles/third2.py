try:
    # Open the file in read mode
    with open('Phone.txt', 'r') as phone_numbers:
        # Initialize the operators' dictionary
        operators = {
            'beeline': [], 'ucell': [], 'uzmobile': [], 'uztelecom': [],
            'humans': [], 'ums': [], 'rostelecom': [], 'mts': [], 'megafon': []
        }

        # Define the mapping of initial digits to operator names
        operator_map = {
            '1': 'beeline', '2': 'ucell', '3': 'uzmobile', '4': 'uztelecom',
            '5': 'humans', '6': 'ums', '7': 'rostelecom', '8': 'mts', '9': 'megafon'
        }

        # Iterate over each line in the file
        for line in phone_numbers:
            # Split the line into parts
            parts = line.strip().split(" ")

            # Get the last element, assumed to be the phone number
            phone_number = parts[-1]

            # Extract the first character of the phone number to identify the operator
            operator_key = phone_number[0]

            # Check if the operator key exists in the mapping
            if operator_key in operator_map:
                # Append the phone number to the correct operator's list
                operators[operator_map[operator_key]].append(phone_number)
            else:
                # Log or handle the unexpected operator key scenario
                print(f"Unknown operator key '{operator_key}' found in line: {line}")

        # Print the operators and their associated phone numbers
        for operator, numbers in operators.items():
            print(f"{operator}: {numbers}")

except FileNotFoundError:
    print("The file 'Phone.txt' was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
