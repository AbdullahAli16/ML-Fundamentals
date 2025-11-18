''' Pandas was created by Wes McKinney in 2008 . He created it because when he used to work
    at AQR Capital Management, he used to face alot of challenges in analayzing large financial
    datasets and existing tools like Excel were inefficient for large-scale data cleaning and analysis'''

""" ⚠️ WARNING: This file and all the other files in this directory contains multiple operations and
print statements for learning purposes. Running it without understanding the code may produce
extensive output. Review the code before execution to understand what each section does. """

# Read data from CSV file into a dataframe

import pandas as pd

# Encoding is the process of converting text into a format that computers can store or read
file = pd.read_csv(r"../Datasets/employees.csv", encoding="latin1")
print(file)

# Note: If you encounter issues while reading the file, use "utf-8" or "latin1" whichever works for you

# For an excel file(.xlsx), use the .read_excel() method and for JSON file, use .read_JSON() etc

data={
    "Name":["Abdullah","Sarim","Saif"],
    "Age":[21,21,23],
    "City":["Hirabad","Latifabad 7 no","Latifabad 9 no"]    
}

# Making our data(dictionary) into a Dataframe
file=pd.DataFrame(data)
print(file)

# Converting the Dataframe into a csv, xlsx, json etc file
file.to_csv("output.csv",index=False)
''' Note: The data and also csv file will contain the index by default but you can
    disable it using index=False '''
    
# Same as earlier, if you want to convert it into an excel file use .to_excel(), and .to_json() for json file etc

""" Steps for Analyzing data:
    1. Explore and understand the dataset 
    2. Identify the problems in the dataset
    3. Plan next steps """

file = pd.read_csv(r"C:\Users\PMYLS\Desktop\Machine Learning\Datasets\employees.csv", encoding="latin1")
print(file)

''' Methods we can apply on the dataset '''

# head --> Display rows from beginning (Top 5 by default)
print(f"Top 10 rows of the dataset are: \n{file.head(10)}")

# tail --> Display rows from end (Bottom 5 by default)
print(f"Bottom 10 rows of the dataset are: \n{file.tail(10)}")

# info --> A method which will give you a consive summary of your dataset
''' Index information : The type of index and its range (e.g. RangeIndex(rows): 0 to 999).
    Column names : Lists all column names.
    Non-null counts  How many non-missing (non-null) entries each column has.
    Dtype (data type) : The data type of each column (int64, float64, object, category, datetime64[ns], etc.).
    Memory usage : How much memory the DataFrame consumes.'''

print(f"The summary of the dataset is:")
file.info()

# Creating your own Dataframe and saving it in a file

file = pd.read_csv(r"C:\Users\PMYLS\Desktop\Machine Learning\Datasets\employees.csv", encoding="latin1")
dataset=file.head(10)

# describe --> It is used to generate summary statistics for your numerical, categorical or all
#               columns in a dataframe
''' Statistic	    Meaning
    count	        Number of non-null values in a column 
    mean	        Average value of a column
    std	            Standard deviation of a column
                    ( A small standard deviation (std) means the data values are close to
                    the mean, while a large std means they are more spread out)
    min	            Minimum value in a column
    25%, 50%, 75%	Percentiles (quartiles) of a column
                    ( Imagine 100 students took a test.
                        25% percentile (Q1): 25 students scored below this mark.
                        50% percentile (Q2): 50 students scored below this mark- that's the median (middle score).
                        75% percentile (Q3): 75 students scored below this mark- only the top 25 students scored higher.)
    max	            Maximum value in a column '''
print(dataset.describe(include='all'))

# shape --> An attribute which returns a tuple containing (no of rows,no of columns) in the dataset
print(f"The size of the dataset is: {dataset.shape}") 

# columns --> An attribute which returns the name of all the columns in the dataset
print(f"The columns are: {dataset.columns}")

# Accessing specific columns of the dataset
print(f"First Name and gender columns of the dataset are: \n{dataset[["First Name","Gender"]]}")

# Filtering specific rows of the dataset using boolean indexing
print(f"Only male employees in the dataset are: \n{dataset[dataset["Gender"]=="Male"]}")
print(f"Only male employees and having salary greater than 65000 in the dataset are: \n{dataset[(dataset["Gender"]=="Male") & (dataset["Salary"]> 65000)]}")

# Use & for AND, | for OR, and ~ for NOT — wrap each condition in parentheses ( )