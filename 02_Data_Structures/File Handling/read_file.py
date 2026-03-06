#--------- Read file------------
file = open("my_data.txt", "r")

# Read the content of the file
content = file.read()

print("File contentis: ")
print(content)

file.close()
