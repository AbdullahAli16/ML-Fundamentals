# Array properties and Operations

import numpy as np
arr=[[1,4,6,8],
     [2,4,7,9],
     [1,2,3,4],]

# shape --> Tells the order(No of rows, no of columns) of an array(matrix)
arr=np.array(arr)
print(f"The arr is: {arr}")
print(f"The order of arr is: {arr.shape}")

# size --> Returns total no of elements in an array
print(f"No of elements in arr is: {arr.size}")

# ndim --> Returns the dimension in an array
""" A single number is known as scalar and it will have zero dimensions
    If we have data that is spread through only a row, it will have 1 dimension
    If we have data that is spread through row and column both , it will have 2 dimensions and so on """

print(f"The dimension of arr is: {arr.ndim}")

# Data types and type Casting in NumPy

"""
Most Common NumPy Data Types (practically used)

- int32   : Standard integer (for whole numbers)
- int64   : Larger integer (often default on 64-bit systems)
- float32 : Decimal numbers (single precision)
- float64 : Decimal numbers (double precision, default)
- bool_   : Boolean values (True / False)
- complex128 : Complex numbers (real + imaginary parts)

If you do not specify a data-type using dtype, NumPy will automatically pick one for you — usually
float64 for decimals and int64 for integers.
"""

# dtype --> Returns the data type of an array
print(f"The datatype of elements in arr is: {arr.dtype}")

# astype --> Change type of an array
""" If we change the data type of a single element in an array the entire arrays becomes of that specific type 
    but there are priorities: int < float < string """
print(f"Current type of arr is: {arr.dtype}")
arr= arr.astype(str)
print(f"New type of arr is: {arr.dtype}")

# Arithmetic Operation on Numpy Arrays

arr= arr.astype(int)  # Converting it again into int type for performing calculations

print(f"The arr is: \n{arr}")
print(f"The arr after adding 5 in each element is: \n{arr+5}")
print(f"The arr after substracting 5 from each element is: \n{arr-5}")
print(f"The arr after multiplying 5 with each element is: \n{arr*5}")
print(f"The arr after dividing 5 with each element is: \n{arr/5}")
print(f"The arr after putting 5 as exponent on each element is: \n{arr**5}")

# Aggregation (Summarization) Functions

print(f"The sum of all elements in arr is: {np.sum(arr)}")
print(f"The average of all elements in arr is: {np.mean(arr)}")
print(f"The largest element of all elements in arr is: {np.min(arr)}")
print(f"The smallest element of all elements in arr is: {np.max(arr)}")
print(f"The standard deviation of all elements in arr is: {np.std(arr)}")
print(f"The variance of all elements in arr is: {np.var(arr)}")