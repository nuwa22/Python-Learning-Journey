# stack
# A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
# The last element added to the stack will be the first one to be removed.

# Stack operations
# 1. Push: Add an element to the top of the stack
# 2. append() method is used to add an element to the end of the list, which represents the top of the stack.
# 3. Pop: Remove the top element from the stack
# 4. Peek: Get the top element from the stack without removing it
# 5. Is Empty: Check if the stack is empty

history_stack = []

history_stack.append("Page 1")
history_stack.append("Page 2")
history_stack.append("Page 3")

print("Current Stack:", history_stack)

last_page = history_stack.pop()
print("Last visited page:", last_page)
print("Current Stack after popping:", history_stack)

