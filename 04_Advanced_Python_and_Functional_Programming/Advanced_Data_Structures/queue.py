# Queue
# FIFO (First In First Out)
# A queue is a linear data structure that follows the First In, First Out (FIFO) principle.
# The first element added to the queue will be the first one to be removed.

# Queue operations
# 1. Enqueue: Add an element to the end of the queue
# 2. append() method is used to add an element to the end of the list, which represents the end of the queue.
# 3. Dequeue: Remove the front element from the queue
# 4. pop(0) method is used to remove the first element from the list, which represents the front of the queue.
# 5. popleft() method from the collections.deque class can also be used to remove the front element from the queue efficiently.
# 6. Peek: Get the front element from the queue without removing it
# 7. Is Empty: Check if the queue is empty

from collections import deque 

print_queue = deque()

print_queue.append("Document 1")
print_queue.append("Document 2")
print_queue.append("Document 3")

first_document = print_queue.popleft()
print("First document to print:", first_document)
print("Current print queue:", print_queue)

