"""
Lesson 9: Computer Tour - File Organizer Solution
"""

import os
import shutil


def organize_by_type(directory):
    """
    Organizes files in the given directory into subdirectories based on file type.

    Parameters:
    directory (str): The path to the directory to organize.
    """
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            # Determine the file extension and create a corresponding folder
            file_type = item.split('.')[-1]
            folder_name = os.path.join(directory, file_type.upper())

            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

            # Move the file into the corresponding folder
            shutil.move(os.path.join(directory, item), folder_name)

    print(f"Files in '{directory}' have been organized by file type.")


# Example usage
directory_path = input("Enter the path to the directory you want to organize: ")
organize_by_type(directory_path)
