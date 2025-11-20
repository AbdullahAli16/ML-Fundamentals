# Module 02: Pandas

Pandas is the primary Python library for data analysis and manipulation. It provides efficient tools for loading, cleaning, transforming, aggregating, and analyzing structured data.

## Topics Covered

### DataFrame Basics
- Reading CSV, Excel, JSON files
- Creating DataFrames from dictionaries
- Exporting to CSV, Excel, JSON
- Exploring data using:
  - head(), tail()
  - info()
  - describe()
  - shape, columns
- Selecting rows and columns
- Boolean filtering

### Data Modification
- Adding new columns
- insert() for custom column placement
- Updating values with loc
- Dropping rows and columns

### Handling Missing Values
- Detecting missing entries: isnull(), notnull()
- dropna() for removing missing data
- fillna() for replacing missing values
- Filling with mean, mode
- Interpolation for numerical estimation

### Grouping, Merging, Sorting
- Sorting with sort_values()
- Grouping data with groupby()
- Aggregations: sum, mean, count, min, max, std
- Merging DataFrames using merge()
- Joining on indexes with join()
- Concatenating DataFrames with concat()

## Notebook Breakdown

- **01_dataframes_basics.ipynb**
  Introduction to DataFrames, reading/writing files, data exploration, filtering

- **02_data_modification.ipynb**
  Adding, inserting, updating, and dropping data

- **03_handling_missing_values.ipynb**
  Detecting, cleaning, replacing, and interpolating missing data

- **04_grouping_merging_sorting.ipynb**
  Sorting, grouping, aggregating, merging, joining, concatenating

## Key Takeaways
- Pandas DataFrames are the standard for data manipulation in Python
- Boolean filtering and indexing provide powerful ways to extract data
- Handling missing values correctly prevents corrupted analysis
- Merging and grouping replicate SQL-like operations inside Python
- Pandas is essential for data cleaning, EDA, feature engineering, and ML pipelines