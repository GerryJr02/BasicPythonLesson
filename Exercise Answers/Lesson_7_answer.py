"""
Lesson 7: Functions Part 1 - Personalized Greeting Card Generator Solution
"""

def create_greeting(name, occasion):
    """
    Generates a personalized greeting message.

    Parameters:
    name (str): The name of the person.
    occasion (str): The occasion for the greeting.

    Returns:
    str: A personalized greeting message.
    """
    return f"Happy {occasion}, {name}! Wishing you all the best on your special day!"

# Asking for user input
user_name = input("Enter your name: ")
occasion = input("Enter the occasion: ")

# Generating and printing the greeting
greeting_message = create_greeting(user_name, occasion)
print(greeting_message)
