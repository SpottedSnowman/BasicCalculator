def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


def clear():
    return None


def calculator():
    print("Welcome to Command Line Calculator!")
    print("Enter 'exit' to quit the calculator.")

    while True:
       
        operation = input("Enter operation (+, -, *, /): ")
        
        
        if operation == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        
        
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.")
            continue
        
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        
        
        print("Result:", result)
        
        
        clear_output = input("Clear output? (yes/no): ")
        if clear_output.lower() == 'yes':
            clear()
        elif clear_output.lower() == 'no':
            continue
        else:
            print("Invalid input. Output not cleared.")


if __name__ == "__main__":
    calculator()
