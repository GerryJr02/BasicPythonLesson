"""
Lesson 9: Computer Tour

Objective:
Develop a script that organizes files in a directory into folders based on file type or date. This
 script will help you understand how Python can interact with the operating system to manage files
  and directories.

Instructions:
1. Choose a directory to organize. For simplicity, you might start with a specific folder like
 'Downloads'.
2. Your script should scan all files in the chosen directory.
3. Decide on an organization criteria:
   - By file type: Group files into folders based on their extension (e.g., 'JPEG', 'PDF').
   - By date: Group files into folders based on their creation or modification date (e.g.,
    'January-2020', 'February-2020').
4. For each file, move it into the corresponding folder. If the folder doesn't exist, create it.
5. Provide feedback to the user, such as "25 files have been organized into 5 folders".

Notes:
- Use the `os` module for navigating directories and handling files.
- Use the `shutil` module for moving files.
- Consider error handling for operations like moving files and creating directories.

Example Output:
'25 files have been organized into 5 folders based on file type.'
"""

# Your code goes here
