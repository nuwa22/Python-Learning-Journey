fruits = ["Apple", "Banana", "Orange", "Mango"]
print(fruits)

# Accessing elements
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# Change List
fruits[1] = "Grapes"
print(fruits)

# Append to List
colors = ["Red", "Green"]
colors.append("Blue") # Appends "Blue" to the end of the list
print(colors)

# Insert to List
colors.insert(1, "Yellow")
print(colors)

# Remove from List
colors.remove("Green")
print(colors)

# Pop from List
colors.pop(0) # Pops "Yellow" index 0
print(colors)

# Length of List
print(len(colors))

# List Slicing
# Slicing syntax: list[start:stop:step]
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# get elements from index 0 to 3
print(my_list[0:3])

# get elements from index 4 to the end
print(my_list[4:])

# get elements from the beginning to index 5
print(my_list[:5])

# get every second element from index 0 to 8
print(my_list[0:9:2])

print(my_list[::2]) # get every second element from the entire list

# Reverse the list
print(my_list[::-1])

print(my_list[-5:]) # get the last 4 elements of the list




