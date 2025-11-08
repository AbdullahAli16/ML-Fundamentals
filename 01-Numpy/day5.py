# Broadcasting, Vectorization and Handling Missing/Special Values

''' Broadcasting is the set of rules numpy uses to perform operations on arrays of different
    shapes by automatically expanding them when possible'''
    
import numpy as np

arr1=np.array([100,200,300])
arr2=np.array([400])

# Here arr2 expands it's shape from (0,0) to (0,2), but keep in mind that this is not possible in every case
result=arr1*arr2
print(f"The Broadcasting result is: {result}")


''' 3 Rules of Broadcasting 

    1. Matching Dimensions
    2. Expanding single elements
    3. Incompatible shapes        '''
    
    
''' Vectorization: Applying operations on all the elements of an array without using loops '''

arr1= np.array([1,2,3])
arr2= np.array([4,5,6])
result=arr1*arr2
print(f"The Vectorization result is: {result}")

arr=np.array([1,2,3,np.nan,5,-np.inf,np.inf])

''' Handling missing/special values '''

# isnan --> Tells which elements in the array are nan(not a number)
print(f"The elements in arr that are nan: {np.isnan(arr)}")

# nan_to_num --> Swaps the nan values in an array with a custom number (0 by default)
print(f"The elements in arr that were nan are now replaced by 2: {np.nan_to_num(arr,nan=2)}")

# isinf --> Checks if a value in the array are infinite
print(f"The elements in arr that are infinity: {np.isinf(arr)}")
print(f"The elements in arr that were infinity are now replaced by 1000 and -1000: {np.nan_to_num(arr,nan=800,posinf=1000,neginf=-1000)}")
