# Indexing, Slicing, Boolean masking and some other concepts

import numpy as np
arr=[1,2,3,4,5]

# Indexing --> Selecting a single element from an array (Negative indexing is also valid)

# 1D- Array:
arr=np.array([1,2,3,4,5])
print(f"At index 2 is the element: {arr[2]} and on index -1 is the element {arr[-1]} in: {arr}")

# 2D- Array:
d2_arr=np.random.randint(1,9,[2,4])
print(f"A random 2D array is: \n {d2_arr} \n at index (0x3) is: {d2_arr[0,2]} and at index(-1,3) is: {d2_arr[-1,0]} ") 
""" Order of matrix (No of rows and columns) starts from zero too """

# Slicing --> Selecting a subset from an array
arr=np.array([1,2,3,4,5,6])
print(f"The arr is: {arr}")
print(f"The part from index 2 to 4 in arr is: {arr[2:4]}") # [Start,end-1,step]
print(f"The part from index 0 to 4 in arr is: {arr[:4]}") 
print(f"The part from index 0 to end in arr is: {arr[0:]}") 
print(f"Every second elememt in arr is: {arr[::2]}") 
print(f"The part from index 4 to 0 (reversed array) in arr is: {arr[::-1]}") 

# Fancy Indexing --> Selecting multiple elements at once
print(f"Printing multiple elements at different indexes (here index no: 1,2,5): {arr[[1,2,5]]}")
# Whenever we do fancy indexing it creates a copy of that data so the original data remains the same

# Boolean slicing --> Lets you filter the elements in the array based on a defined condition
print(f"Elements greater than 2 in arr are: {arr[arr>2]}")

# Reshaping and Manipulating Arrays

# reshape --> Changes shape of an array without modifying the data present in that array
#  (Ex: Converting a 1D array into 2D array) (Only converts lowerD array into upperD array)
arr1=np.array([1,2,3,4,5,6,7,8])
print(f"arr1 is: {arr1}")
reshaped_arr=arr1.reshape(2,4)
print(f"arr1 is now: \n {reshaped_arr}")

""" Total no of elements should be same (ex: if a 1D array has 8 elements, we can only make 
    arrays that also have 8 elements in total like a 2D(2x4) matrix and we cant make a 3D(3x3)
    matrix because it has 9 elements in total and we only have 8 """

print(f"Reshape method is a view, so it can change the original values of arr1 but not the order: \n{arr1}")
print(f"but only the reshaped array: \n{reshaped_arr}")

""" --- A VIEW OF AN ARRAY BASICALLY MEANS THAT IT IS A REFRENCE TO THE ORIGINAL ARRAY AND ANY
        CHANGES THAT YOU MAKE REGARDING "VALUES" IN THE VIEW, WILL BE AUTOMATICALLY IMPLEMENTED IN
        THE ORIGINAL ARRAY TOO BECAUSE THE ORIGINAL AS WELL AS THE VIEW ARE BOTH REFRENCING FROM
        THE SAME MEMORY BLOCK --- """

# Flattening arrays

# reval --> Changes shape of an array without modifying the data present in that array
#  (Ex: Converting a 2D array into 1D array) (Only converts upperD array into lowerD array)

# flatten --> Does the same function of ravel
""" The main difference between ravel and flatten is that ravel creates a view which will affect
    the original value of the array but flatten creates a copy and the original value of the
    array remains same """

arr = np.array([[1,2,3,4],
                [5,6,7,8]])

print(f"Original array before modification: \n{arr}")

rvl = arr.ravel()
flt = arr.flatten()

rvl[0] = 100
flt[1] = 200

print(f"Original array after modification: \n{arr}")
""" Notice that in the original array only the ravel's value was inserted, while flatten's value was
     only inserted in its own copy """

print(f"Ravelled array (view): {rvl}")
print(f"Flattened array (copy): {flt}")