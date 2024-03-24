"""
Lesson 4: If-Else Branching - Adventure Game Solution
"""

print("Welcome to the adventure game!")
print("You find yourself at the edge of a dark forest.")
choice1 = input("Will you enter the forest or walk around it? (enter/walk) ").lower()

if choice1 == "enter":
    print("As you walk into the forest, you encounter a fork in the path.")
    choice2 = input("Do you go left or right? (left/right) ").lower()

    if choice2 == "left":
        print("You've found a hidden treasure chest! Game over. You win!")
    elif choice2 == "right":
        print("You've walked into a spider's web and are stuck forever. Game over. You lose!")
    else:
        print("Invalid choice. Lost in the forest, you wander forever. Game over.")

elif choice1 == "walk":
    print("You've successfully walked around the forest and reached your destination. Game over."
          " You win!")
else:
    print("Invalid choice. You're lost forever. Game over.")

