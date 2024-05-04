def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

print("Welcome to the Calculator!")

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation. Please try again.")
            continue
        
        print("Result: ", result)
    except ValueError:
        print("Please enter valid numbers.")
    except Exception as e:
        print("An error occurred:", e)

    choice = input("Do you want to perform another calculation? (yes/no): ")
    if choice.lower() != 'yes':
        print("Thank you for using JOSEPH LARBI'S' Calculator!")
        break