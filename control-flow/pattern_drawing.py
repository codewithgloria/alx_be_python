# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks in each column of the current row
    for col in range(size):
        print("*", end="")  # Print without moving to a new line
    print()  # Move to the next line after the row is complete
    row += 1