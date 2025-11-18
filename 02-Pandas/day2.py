# Data Modification

import pandas as pd
file=pd.read_csv(r"../Datasets/employees.csv", encoding="latin1")
dataset=file.head(10)
dataset2=file.tail(10)
print(f"Dataset currently is: \n{dataset}")

# Adding a new column in the dataset

dataset["AGE"]=26       # Adds the column in the end of the dataset
# print(f"Adding AGE column in the dataset: \n{dataset}")

# insert --> A method used for adding columns on specific positions
dataset.insert(0,"City","Hyderabad")
print(f"Adding CITY column in the dataset: \n{dataset}")

# Updating values

# loc --> Selecting a specific cell, rows and columns
dataset.loc["City"]="Constantinpole"
print(f"The updated dataset now is: \n{dataset}")

# Deleting existing columns or rows from the dataset 

dataset.drop(columns=["First Name"], inplace=True) 
# (inplace=True) changes the original dataset and (inplace=false) returns a new dataframe
print(f"Dataset after dropping the 'First Name' column is: \n{dataset}")

# Handling Missing Values

# isnull --> Returns a boolean dataframe indicating which value is null and which one is not
print(f"The boolean version of the dataset indicating about the null values: \n{dataset.isnull()}")
print(f"The count of the null values in the dataset: \n{dataset.isnull().sum()}")

# dropna --> Drop all rows/columns with missing values
dataset.dropna(axis=0,inplace=True)
print(f"The dataset after dropping missing valued rows and column is: \n{dataset}")

# fillna --> Replace all the missing values with a defined value or set of values
dataset.fillna(0,inplace=True)
print(f"The dataset after replacing missing values from rows and columns with 0 is: \n{dataset}")

# Choosing the average mean value in the column (For numeriacl-based columns)
dataset["Salary"].fillna(dataset["Salary"].mean(),inplace=True)
print(f"Replacing the values with average mean of the other values: {dataset}")

# Choosing the most common value in the column (For string-based columns)
dataset["Team"].fillna(dataset["Team"].mode()[0],inplace=True)
print(f"Replacing the values with common value among the other values: {dataset}")

# interpolate --> Fills missing values by estimating them using linear, polynomial, or time-based interpolation methods (only for numerical based columns)
import numpy as np
dataset.loc[0,"Salary"]=np.nan
dataset.interpolate(method="linear",axis=0,inplace=True)
print(f"After interpolation the dataset is: \n{dataset}")
# Do check out the other methods too like "polynomial","time" etc 

# Sorting the data

# sort_values --> Sorts the rows in a column in ascending/descending order
dataset.sort_values(by=["Bonus %"],ascending=True, inplace=True)
print(f"The dataset now is: \n{dataset}")
""" If you are sorting more than one columns at a time, you need to pass a separate ascending
    value for each column """ 
    
# Grouping the data

# groupby --> Creates groups based on the unique values in the specified column
grouped=dataset.groupby("Team")["Salary"].sum()
print(f"This shows that the employees working in a specific team are taking up how much salary in total: \n{grouped}")
# For multiple columns
grouped=dataset.groupby(["Team","First Name"])["Salary"].sum()
print(f"This shows that the employees working in a specific team and have specific names are taking up how much salary in total: \n{grouped}")

""" Some common aggregation functions are:
    1- sum() -> Returns the total sum of all the values
    2- mean() -> Returns average of the values
    3- count() -> Returns count of NaN values
    4- min() -> Returns the minimum value
    5- max() -> Returns the maximum value
    6- std() -> Returns standard deviation """
    
# Merging and Joining the data

# merge --> Combines two DataFrames based on one or more common columns (like SQL joins)
departments = pd.DataFrame({
    "Team": ["Finance", "Engineering", "HR", "Marketing"],
    "Manager": ["Alice", "Bob", "Carol", "David"]
})

merged = pd.merge(dataset, departments, on="Team", how="left")
print(f"This shows that every employee is now assigned to their respective manager based on team:\n{merged}")

""" Common 'how' options for merging:
    1- inner  -> Keeps only rows that exist in both DataFrames
    2- left   -> Keeps all rows from the left DataFrame, adds matches from the right
    3- right  -> Keeps all rows from the right DataFrame, adds matches from the left
    4- outer  -> Keeps all rows from both, fills missing with NaN
"""

# join --> Combines two DataFrames based on their index instead of column
bonus_data = pd.DataFrame({
    "First Name": ["John", "Jane", "Emily"],
    "Bonus Points": [120, 150, 100]}).set_index("First Name")

joined = dataset.join(bonus_data, on="First Name", how="left")
print(f"This shows that the employees now have their bonus points joined by their first names:\n{joined}")

""" Difference between merge() and join():
    merge() -> Uses column(s) for combining
    join()  -> Uses index for combining
"""

# concat --> Combines dataframes vertically or horizontally
print(f"Concatenation of two datasets is: \n{pd.concat([dataset,dataset2], axis=0, ignore_index=True)}")

