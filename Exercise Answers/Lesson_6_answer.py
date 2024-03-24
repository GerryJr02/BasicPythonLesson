"""
Lesson 6: Nested Loops - Pyramid Pattern Solution
"""

# Asking the user for the size of the pyramid
size = int(input("Enter the size of the pyramid: "))

for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end = '')  # Print numbers on the same line
    print()  # Move to the next line after each row
