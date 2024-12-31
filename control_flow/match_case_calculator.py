# Match case calculator

# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get user input for operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using match case
result = match operation:
    case "+":
        return num1 + num2
    case "-":
        return num1 - num2
    case "*":
        return num1 * num2
    case "/":
        if num2 == 0:
            return "Cannot divide by zero."
        else:
            return num1 / num2
    case _:
        return "Invalid operation."

# Print the result
print(f"The result is {result}")
