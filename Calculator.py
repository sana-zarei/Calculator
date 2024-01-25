import os

def calculate():
    """ Simple calculator function to perform basic arithmetic operations."""
    # Clear the screen for better user experience
    os.system('cls' if os.name == 'nt' else 'clear')

    # Prompt user to choose an operation
    operation = input(''' Please choose an operation : \n + for addition \n - for subtraction \n * for multiplication \n / for division \n Enter your choice : ''')

    # Prompt user for numbers
    number_1 = float(input('Enter The First Number : '))
    number_2 = float(input('Enter The Second Number : '))

    # Perform the chosen operation
    if operation == '+':
        result = number_1 + number_2
        print(f'{number_1} + {number_2} = {result}')

    elif operation == '-':
        result = number_1 - number_2
        print(f'{number_1} - {number_2} = {result}')

    elif operation == '*':
        result = number_1 * number_2
        print(f'{number_1} * {number_2} = {result}')

    elif operation == '/':
        # Check for division by zero
        if number_2 == 0:
            print("Cannot divide by zero.")
        else:
            result = number_1 / number_2
            print(f'{number_1} / {number_2} = {result}')

    else:
        print('Invalid operator, please try again.')

# Call calculate function
if __name__ == "__main__":
    calculate()