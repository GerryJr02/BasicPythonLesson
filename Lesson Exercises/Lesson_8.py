"""
Lesson 8: Functions Part 2

Objective:
Revise the Math Quiz program to generate simple arithmetic quizzes (addition, subtraction) with
 a twist: the type of operation (addition or subtraction) should be chosen randomly for each
 question. The quiz difficulty should still adjust based on the user's performance, increasing
 after correct answers and decreasing after incorrect answers.

Instructions:
1. Define a function `generate_quiz` that takes one parameter: `level` (with a default value
 indicating the starting difficulty level).
2. Inside the function, use the `level` parameter to determine the range of numbers for the quiz
 questions. The range should increase with higher levels.
3. Randomly select an arithmetic operation (addition or subtraction) for each quiz question.
4. After generating and displaying a question, prompt the user for their answer and provide
 immediate feedback.
5. Adjust the difficulty level based on the user's answer: increase the level after a correct answer
 and decrease it after an incorrect answer (ensure the level does not go below 1).
6. Loop to continue generating questions, adjusting the level and randomly selecting the operation
 each time.

Notes:
- This exercise further explores advanced function concepts and introduces randomness into the
 function's behavior.
- The randomness adds variety and makes each run of the quiz unique.

Example Output:
What is 5 + 3? 8
Correct! Let's try something a bit harder.
What is 17 - 9? 7
Incorrect. The answer is 8. Let's try an easier one.
"""

# Your code goes here
