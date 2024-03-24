"""
Lesson 5: Loops

Objective:
Develop a number guessing game where the user has to guess a randomly selected number within a
 certain number of attempts.

Instructions:
1. Use the random module to generate a random number between 1 and 100 at the start of the game.
2. Ask the user to guess the number. Collect their guess with input().
3. Use a loop to give the user a total of 5 attempts to guess the number.
4. After each guess, tell the user if their guess is too high, too low, or correct.
5. If the user guesses the number correctly, congratulate them and end the game.
6. If the user fails to guess the number after 5 attempts, tell them the correct number and end the
 game.

Notes:
- Use the randint function from the random module to generate the random number.
- Pay attention to converting the input from the user into an integer before comparison.
- Consider using a while loop for the attempts, and use a variable to track the number of tries.

Example Interaction:
Guess the number between 1 and 100: 50
Too high!
Guess again: 25
Too low!
Guess again: 37
Correct! You guessed the number in 3 tries.
"""

# Your code goes here
