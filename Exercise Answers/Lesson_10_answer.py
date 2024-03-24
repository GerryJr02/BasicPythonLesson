"""
Lesson 10: Conditional Expressions - Customized Message Filter Solution
"""


def filter_messages(messages, keyword):
    """
    Filters a list of messages based on the presence of a keyword.

    Parameters:
    messages (list of str): The list of messages to filter.
    keyword (str): The keyword to filter messages by.

    Returns:
    list of str: A list of messages containing the keyword.
    """
    return [message for message in messages if keyword in message]


# Prompting user input for messages and filter criteria
user_messages = input("Enter your messages (separated by commas): ").split(',')
filter_keyword = input("Enter a word to filter messages by: ")

# Filtering messages
filtered_messages = filter_messages(user_messages, filter_keyword.strip())

# Printing filtered messages
print("Filtered messages:", filtered_messages)
