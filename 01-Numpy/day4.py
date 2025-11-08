# Array Modification

import numpy as np

""" We can directly apply operations on lists in python, however arrays in numpy have a fixed size
    so in order to perform calculations we have to create a separate array so the original arrays 
    remains the same """

# insert --> inserts an element at a specifix index in an array
arr= np.array([1,2,3,4,5])
new_arr=np.insert(arr,5,6,axis=0) # (arr,index,value,axis(0 if row-wise and 1 if column-wise))
print(f"[INSERT] Original array: {arr} and new_arr: {new_arr}")

d2_arr=np.array([[1,2,3],
                 [4,5,6]])
new_d2_arr=np.insert(d2_arr,1,[10,11],axis=1)
# If we pass axis=None it will insert the elements in the arr in the flatten version
print(f"[INSERT] Original array before inserting: \n{d2_arr} \nand new_arr after inserting: \n{new_d2_arr}")

# append --> adding an element from the end
arr= np.array([1,2,3,4,5])
new_arr=np.append(arr,6) # (arr,index,value,axis(0 if row-wise and 1 if column-wise))
print(f"[APPEND] Original array: {arr} and new_arr: {new_arr}")

d2_arr=np.array([[1,2,3],
                 [4,5,6]])
new_d2_arr=np.append(d2_arr,[[10],[11]],axis=1) # Column-wise
print(f"[APPEND] Original array before appending: \n{d2_arr} \nand new_arr after appending: \n{new_d2_arr}")

new_d2_arr=np.append(d2_arr,[[10,11,12]],axis=0) # Row-wise
print(f"[APPEND] Original array before appending: \n{d2_arr} \nand new_arr after appending: \n{new_d2_arr}")

# concatenate --> merging 2 arrays together
arr1=np.array([[1,2,3]])
arr2=np.array([[4,5,6]])
new_arr=np.concatenate((arr1,arr2), axis=0) # Row-wise (Stacking vertically)
print(f"[CONCATENATE] Row-wise (Stacking horizontally)) \narr1 is: {arr1} ,arr2 is {arr2} and The new arr is: \n{new_arr}")

arr1=np.array([[1],[2],[3]])
arr2=np.array([[4],[5],[6]])
new_arr=np.concatenate((arr1,arr2), axis=1) # Column-wise (Stacking horizontaly)
print(f"[CONCATENATE] (Column-wise (Stacking vertically)) \narr1 is: {arr1} ,arr2 is {arr2} and The new arr is: \n{new_arr}")

# delete --> removes an element at a specified index
arr=np.array([1,2,3])
new_arr=np.delete(arr,0)
print(f"[DELETE] The new arr is: {new_arr}")

arr1=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
new_arr=np.delete(arr1,0,axis=1) # Column-wise
print(f"[DELETE] The new arr after deleting a column is: \n{new_arr}")

new_arr=np.delete(arr1,0,axis=0) # Row-wise
print(f"[DELETE] The new arr after deleting a row is: \n{new_arr}")

new_arr=np.delete(arr1,[0,2],axis=1) # Multiple columns
print(f"[DELETE] The new arr after deleting multiple columns [0,2]: \n{new_arr}")

# stack --> joins arrays along a new axis
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

new_arr = np.stack((arr1, arr2), axis=0)
print(f"[STACK] Stacking along a new axis=0: \n{new_arr}")

#  hstack --> stacks arrays horizontally (side by side)
new_arr = np.hstack((arr1, arr2))
print(f"[HSTACK] Stacking arrays horizontally (side by side): \n{new_arr}")

#  vstack --> stacks arrays vertically (one on top of the other)
new_arr = np.vstack((arr1, arr2))
print(f"[VSTACK] Stacking arrays vertically (one on top of another): \n{new_arr}")

#  dstack --> stacks arrays along depth (creates 3D array)
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
arr2 = np.array([[7, 8, 9],
                 [10, 11, 12]])
new_arr = np.dstack((arr1, arr2))
print(f"[DSTACK] Stacking arrays along depth (3D stacking): \n{new_arr}")

# split --> splits an array into sub-arrays
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
new_arr = np.split(arr, 2, axis=0)  # axis=0 → split between rows, axis=1 → split between columns
print(f"[SPLIT] Splitting an array: \n{new_arr}")

# hsplit --> splits arrays horizontally (along columns)
""" It cuts the array vertically, creating sub-arrays side by side """
new_arr = np.hsplit(arr, 3)
print(f"[HSPLIT] Splitting arrays horizontally (along columns): \n{new_arr}")

# vsplit --> splits arrays vertically (along rows)
""" It cuts the array horizontally, creating sub-arrays stacked on top of each other """
new_arr = np.vsplit(arr, 2)
print(f"[VSPLIT] Splitting arrays vertically (along rows): \n{new_arr}")

# dsplit --> splits arrays along depth (axis=2)  P.S Used only for 3D arrays
arr = np.array([[[1, 2, 3],
                 [4, 5, 6]],
                [[4, 5, 6],
                 [7, 8, 9]]])

new_arr = np.dsplit(arr, 3)
print(f"[DSPLIT] Splitting arrays along depth (3D splitting): \n{new_arr}")