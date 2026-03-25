import os

# Get the current working directory
current_path = os.getcwd()
print(f"Current working directory: {current_path}")

# List all files and directories in the current working directory
items = os.listdir()
print(f"All files and directories in the current working directory: {items}")

# Create a new directory
new_dir = os.mkdir("My_Secret_Folder")

items = os.listdir()
print(f"All files and directories in the current working directory: {items}")