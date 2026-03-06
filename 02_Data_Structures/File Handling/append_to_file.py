#---------Append file------------
file = open("my_data.txt", "a")

file.write("This line is appended to the file.\n")

file.close()
print("Data appended successfully.")