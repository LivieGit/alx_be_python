# Pattern drawing using nested loops

# Get user input for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
for row in range(size):
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after each row
