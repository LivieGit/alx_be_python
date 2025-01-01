# Get user input for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Initialize column counter
    col = 0

    # Inner while loop for columns
    while col < size:
        print("*", end="")  # Print asterisk without newline
        col += 1

    # Move to the next line after each row
    print()
    row += 1
