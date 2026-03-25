from pathlib import Path
# this is new in Python 3.4, it provides an object-oriented interface for working with file system paths.
# find the current directory
current_dir = Path.cwd()
print(f"Current directory: {current_dir}")

# create a new directory
secret_folder = current_dir / "My_Secret_Folder" / "secret_message.txt"
print(f"New directory path: {secret_folder}")

# write a new file
secret_folder.write_text("This is a secret message.")
print("file created successfully")


# read a file
content = secret_folder.read_text()
print(f"Secret message: {content}")


# find file
for file in current_dir.glob("*.py"):
    print(f"Python file found: {file}")