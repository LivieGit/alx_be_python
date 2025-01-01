# Multiplication table generator

# Get user input for the number
number = int(input("Enter a number to see its multiplication table: "))

# Print the multiplication table header
print(f"Multiplication table for {number}:")

# Generate the multiplication table using a for loop
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
