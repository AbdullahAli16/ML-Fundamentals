""" Numpy stands for Numerical Python and it is created in C language that's why it is much faster
     compared to normal lists. """

""" ⚠️ WARNING: This file and all the other files in this directory contains multiple operations and
print statements for learning purposes. Running it without understanding the code may produce
extensive output. Review the code before execution to understand what each section does. """

# Numpy arrays are faster, memory efficient have lots of functions (apart from built-in ones)
import numpy as np

# Difference between python list and Numpy array
a=[1,2,3,"hello"]
print(f"Regular list: {a}")
a= np.array(a)
print(f"Numpy array: {a}")

# We can create an array manually and choose values of our choice
arr=np.array([2,3,4,5,6])


# Methods of arrays in NumPy

# arange --> for range
natural_num=np.arange(0,10) # Start, stop and step
print(f"Array of natural numbers: {natural_num}") 
# Notice how there are no commas in between
# Type of natural_num is: <class 'numpy.ndarray'> (Numpy array)

# linspace --> for equal values in between a range
numbers= np.linspace(0,1,10) # Start of range, end of range, no of values between range
print(f"10 number values in the range of 0-1 are: {numbers}")
 
# logspace --> logarithmic scale array function
arr= np.logspace(1,3,5) # Start of power of 10(by default you can also specify), end of power of 10, no of values between range
print(f"Logspace: {arr}")

""" One major difference between linspace and logspace is that linspace add the same amount of value in each
     number so the difference(substraction) between each point like from B-->A and C--> B are the same
      while in logspace the ratio between each point like B/A and C/B are same """
      
# zeros --> creates an array of zeros
zeros_arr=np.zeros(5) # No of zeros in an array
print(f"Array of zeros: {zeros_arr}")

# We can create a matrix using NumPy arrays

two_d_matrix=np.zeros([2,3]) # No of rows, no of columns
print(two_d_matrix)

# ones --> creates an array of ones (We can also specify data type in a matrix (which is float by default) )
ones_arr=np.ones([3,3],dtype=int) # No of ones in an array
print(f"Array of ones: {ones_arr}")

# full --> creates an array with values of our choice
full_arr=np.full([2,10],2) # Rows, columns, value
print(f"Array of 2 rows and 10 columns of digit 2:\n{full_arr}")

# eye --> creates an identity matrix
eye_arr=np.eye(2,5) # Rows,columns
print(f"An identity matrix: \n{eye_arr}")

# empty --> Uninitialized array (creating an array without setting any values)
emp_arr=np.empty([2,3])
print(f"Empty array: {emp_arr}")

# random.rand --> Generate random floats (from 0 to 1)
rand_arr=np.random.rand(2,2)
print(f"Array of random numbers between 0-1 is: \n{rand_arr}")

# random.randn --> Random floats from standard normal distribution (from -3 to +3) 
#  and the values are centered around 0 meaning the average (mean) of all values is zero

rand_arr2=np.random.randn(2,2)
print(f"Array of random numbers between -3 to +3 is: \n{rand_arr2}")

# random.randint --> Random integers  
rand_int=np.random.randint(1,10,size=[2,5]) # Start, end, size=(dimension)
print(f"Array of integers is: \n{rand_int}")
