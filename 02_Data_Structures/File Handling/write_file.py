# We can use 3 modes to open files:
# 1. Read (r)
# 2. Write (w)
# 3. Append (a)

# ---------Write file------------
# Open a file
file = open("my_data.txt", "w")

# Write data to the file
file.write("Hello World\n")
file.write("This is a file handling example.\n")

file.close()  # Always close the file after you're done
print("File saved successfully.")
