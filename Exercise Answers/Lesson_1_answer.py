"""
Solution to the Lesson 1: Greeting Program
"""

# Asking for the user's name
user_name = input("What is your name? ")

# Asking for the user's age
user_age = input("How old are you? ")

# Converting the age from string to integer
user_age_int = int(user_age)

# Calculating the age in 5 years
age_in_5_years = user_age_int + 5

# Printing the greeting and the age message
print(f"Hello {user_name}, nice to meet you!")
print(f"In 5 years, you will be {age_in_5_years} years old.")
