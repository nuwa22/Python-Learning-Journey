# List
number_list = [10, 20, 30, 10, 40, 20, 50, 10]
print("number_list:", number_list)

# Set
# A set is an unordered collection of unique items.
# It is defined using curly braces {} or the set() constructor.

unique_numbers = set(number_list)
print("unique_numbers:", unique_numbers)

# Adding an element to a set
# we use the add() method to add an element to a set. If the element already exists, it will not be added again.
unique_numbers.add(60)
print("unique_numbers after adding 60:", unique_numbers)

# adding a duplicate element to a set
unique_numbers.add(10)
print("unique_numbers after adding duplicate 10:", unique_numbers)



# -----------------------------------------------------------------

visitors = ["Suresh", "Kamal", "Nimal", "Suresh", "Amal", "Kamal", "Sunil"]
unique_visitors = set(visitors)

print("Unique Visitors:", unique_visitors)
print("Number of Unique Visitors:", len(unique_visitors))