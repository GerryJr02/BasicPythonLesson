"""
Lesson 8: Functions Part 2 - Math Quiz Solution with Random Operation Switching
"""

import random


def generate_quiz(level=1):
    """
    Generates a math quiz question based on the current level and randomly selects an operation.
    Adjusts the level based on the user's answer.

    Parameters:
    level (int): The current difficulty level of the quiz.

    Returns:
    int: The updated level after the quiz question.
    """
    # Generate numbers based on the level
    num1 = random.randint(level, level * 10)
    num2 = random.randint(level, level * 10)

    # Randomly choose an operation
    operation = random.choice(['addition', 'subtraction'])

    # Generate a question based on the operation
    if operation == 'addition':
        correct_answer = num1 + num2
        user_answer = int(input(f"What is {num1} + {num2}? "))
    else:  # 'subtraction'
        correct_answer = num1 - num2
        user_answer = int(input(f"What is {num1} - {num2}? "))

    # Check the answer and adjust the level
    if user_answer == correct_answer:
        print("Correct! Let's try something a bit harder.")
        return level + 1
    else:
        print(f"Incorrect. The answer is {correct_answer}. Let's try an easier one.")
        return max(level - 1, 1)  # Ensure level does not go below 1


# Main program loop
level = 1
while True:
    level = generate_quiz(level=level)
