import math
import numpy as np

a = np.array([[
    1, 2, 3],
    [4, 5, 6]])

print(a.shape)

# array fundamentals
array_01 = np.array([1, 2, 3, 4, 5, 6])
print(array_01)

# accessing elements
print(array_01[0])

# change elements
array_01[0] = 10
print(array_01)

# slicing
print(array_01[:3])

# slicing creates a view, not a copy
array_02 = array_01[3:]
print(array_02)

array_02[0] = 40
print(array_01)

#Array attributes

array_03 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# ndim
print(array_03.ndim)

# shape
print(array_03.shape)
print(len(array_03.shape) == array_03.ndim)

# size
print(array_03.size)
# size should be the product of the shape dimensions. math is a module and prod is a function that
# returns the product of all elements in an iterable
print(array_03.size == math.prod(array_03.shape))

# dtype
print(array_03.dtype)

# create arrays
# np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace()

# create an array of zeros with shape (2,)
zero_array = np.zeros(2)
print(zero_array)

# create an array of ones with shape (2,)
ones_array = np.ones(2)
print(ones_array)

# create an empty array with shape (2,)
empty_array = np.empty(2)
print(empty_array)

# create an array with values from 0 to 3
arange_array = np.arange(4)
print(arange_array)

# create an array with values from 2 to 8 with step 2
arrange_array_2 = np.arange(2, 9, 2)
print(arrange_array_2)

# create an array with 5 values evenly spaced between 0 and 10
linspace_array = np.linspace(0, 10, num=5)
print(linspace_array)

# specify the data type of an array
x = np.ones(2, dtype=np.int64)
print(x)