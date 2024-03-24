"""
Lesson 5: Loops - Number Guessing Game Solution
"""

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 8

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Main game loop
guess = 0
while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed the number in {attempts} tries.")
        break

if attempts == max_attempts and guess != secret_number:
    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

