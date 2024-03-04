# Getting user input
user_initial_input = input(f"What is the initial amount in the cash register?")
user_input = input(f"What is the amount you would like to input?")


# Declaring a total amount
counter = 0
initial_input = 0
input_amount = 0
total_amount = 0

# Creating a while loop
while user_input != "LOGOFF":

    # Checking to make sure the initial amount is an integer
    if user_initial_input.isdigit():
        initial_input = int(user_initial_input)

    # Checks to see if there is a negative in string
    elif "-" in user_initial_input:
        user_initial_input.replace('-', '')
        initial_input = int(user_initial_input)
        initial_input = -abs(initial_input)

    # If the string does not contain numbers
    else:
        print(f"Please enter a valid initial amount")
        user_initial_input = input(f"What is the initial amount in the cash register")
        initial_input = int(user_initial_input)

    # Checking to make sure the inputted amount is an integer
    if user_input.isdigit():
        input_amount = int(user_input)
        counter += 1

    # Checks to see if there is a negative in string
    elif "-" in user_input:
        user_input.replace('-', '')
        input_amount = int(user_input)
        input_amount = -abs(input_amount)
        counter += 1

    # If the string does not contain numbers
    else:
        print(f"Please enter a valid amount")
        user_input = input(f"What is the amount you would like to input?")
        input_amount = int(user_input)

    # Math behind the entire problem
    if counter < 1:
        total_amount = initial_input + input_amount
        initial_input = 0
        print(f"The total is ${total_amount}")
        user_input = input(f"What is the next amount?")
        # Check to see if it should stop
        user_input = user_input.upper()

    if counter > 1:
        total_amount = total_amount + input_amount
        print(f"The total is ${total_amount}")
        user_input = input(f"What is the next amount?")
        # Check to see if it should stop
        user_input = user_input.upper()

# Should print the final amount after Logoff is typed
print(f"Thank you for logging off,")
print(f"The total is ${total_amount}")
