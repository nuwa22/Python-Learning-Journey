student = {
    "name" : "Suresh",
    "age" : 20,
    "city" : "Colombo",
    "is_student" : True
}

print(student["name"])
print(student["age"])

# use .get() method to access value
print(student.get("city"))
print(student.get("country", "Country not found")) # returns "Country not found" if key "country" is not found

# Change value
student["age"] = 26

# Add new key-value pair
student["job"] = "Software Engineer"
print(student)

# Remove key-value pair
# we can get removed value using pop()
is_student = student.pop("is_student", "Key not found")
print(is_student)

# use del keyword
del student["city"]
print(student)

# use for loop to iterate through dictionary
# get only keys
for key in student.keys():
    print(key)

# get only values
for value in student.values():
    print(value)

# get both keys and values
for key, value in student.items():
    print(f"{key} : {value}") # f-string to format the output

# check length of dictionary
print(len(student))