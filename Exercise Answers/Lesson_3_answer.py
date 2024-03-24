"""
Lesson 3: List Basics - Shopping List Solution
"""

# Starting with an empty shopping list
shopping_list = []


# Function to display the menu
def display_menu():
    print("\nWhat would you like to do?")
    print("Options: Add, Remove, Show, Quit")


# Main program loop
while True:
    display_menu()
    choice = input("> ").capitalize()

    if choice == "Add":
        item = input("What item would you like to add? ").capitalize()
        if item in shopping_list:
            print(f"{item} is already in the shopping list.")
        else:
            shopping_list.append(item)
            print(f"{item} added to the shopping list.")

    elif choice == "Remove":
        item = input("What item would you like to remove? ").capitalize()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")

    elif choice == "Show":
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

    elif choice == "Quit":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose again.")
