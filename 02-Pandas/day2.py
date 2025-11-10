# Data Modification

import pandas as pd
file=pd.read_csv(r"C:\Users\PMYLS\Desktop\Machine Learning\Datasets\employees.csv", encoding="latin1")
dataset=file.head(10)
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


