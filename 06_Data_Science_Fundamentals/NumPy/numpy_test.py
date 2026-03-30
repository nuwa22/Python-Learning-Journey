import math
import numpy as np

a = np.array([[
    1, 2, 3],
    [4, 5, 6]])

print(f"Shape of array 'a': {a.shape}")

# array fundamentals
array_01 = np.array([1, 2, 3, 4, 5, 6])
print(f"Array 'a': {array_01}")

# accessing elements
print(f"First element of array 'a': {array_01[0]}")

# change elements
array_01[0] = 10
print(f"Array 'a' after changing first element: {array_01}")

# slicing
print(f"First three elements of array 'a': {array_01[:3]}")

# slicing creates a view, not a copy
array_02 = array_01[3:]
print(f"Array 'a' slice: {array_02}")

array_02[0] = 40
print(f"Array 'a' after modifying slice: {array_01}")

#Array attributes

array_03 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# ndim
print(f"Number of dimensions in array 'a': {array_03.ndim}")

# shape
print(f"Shape of array 'a': {array_03.shape}")
print(f"Length of shape tuple: {len(array_03.shape)}")
print(f"Shape tuple equals number of dimensions: {len(array_03.shape) == array_03.ndim}")

# size
print(f"Size of array 'a': {array_03.size}")
# size should be the product of the shape dimensions. math is a module and prod is a function that
# returns the product of all elements in an iterable
print(f"Size equals product of shape dimensions: {array_03.size == math.prod(array_03.shape)}")

# dtype
print(f"Data type of array 'a': {array_03.dtype}")

# create arrays
# np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace()

# create an array of zeros with shape (2,)
zero_array = np.zeros(2)
print(f"Array of zeros: {zero_array}")

# create an array of ones with shape (2,)
ones_array = np.ones(2)
print(f"Array of ones: {ones_array}")

# create an empty array with shape (2,)
empty_array = np.empty(2)
print(f"Empty array: {empty_array}")

# create an array with values from 0 to 3
arange_array = np.arange(4)
print(f"Array with values from 0 to 3: {arange_array}")

# create an array with values from 2 to 8 with step 2
arrange_array_2 = np.arange(2, 9, 2)
print(f"Array with values from 2 to 8: {arrange_array_2}")

# create an array with 5 values evenly spaced between 0 and 10
linspace_array = np.linspace(0, 10, num=5)
print(f"Array with 5 values evenly spaced between 0 and 10: {linspace_array}")

# specify the data type of an array
x = np.ones(2, dtype=np.int64)
print(f"Array with specified data type: {x}")

# Adding, removing, and sorting elements
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

# sort the array
sorted_arr = np.sort(arr)
print(f"Sorted array: {sorted_arr}")

# argsort
sorted_indices = np.argsort(arr)
print(f"Indices of sorted array: {sorted_indices}")

# concatenate two arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

concatinated_arr = np.concatenate((arr1, arr2))
print(f"Concatenated array: {concatinated_arr}")

arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6],])
concatinated_arr_2 = np.concatenate((arr3, arr4), axis=0)
print(f"Concatenated array along axis 0: {concatinated_arr_2}")

# reshape an array
arr5 = np.arange(6)
print(f"Original array: {arr5}")

reshaped_arr = arr5.reshape(3, 2)
print(f"Reshaped array: {reshaped_arr}")


reshaped_arr2 = np.reshape(arr5, shape=(2, 3), order='C')
print(f"Reshaped array with order 'C': {reshaped_arr2}")

reshaped_arr3 = np.reshape(arr5, shape=(2, 3), order='F')
print(f"Reshaped array with order 'F': {reshaped_arr3}")

reshaped_arr4 = np.reshape(arr5, shape=(2, 3), order='A')
print(f"Reshaped array with order 'A': {reshaped_arr4}")