# Module 01: NumPy

NumPy (Numerical Python) is the foundational library for numerical computing in Python. Built in C, it provides fast array operations and mathematical functions essential for Machine Learning.

## 📋 Topics Covered

### Array Creation & Initialization
- Creating arrays manually and from ranges
- Special array functions: `arange()`, `linspace()`, `logspace()`
- Generating zeros, ones, and filled arrays
- Identity matrices and empty arrays
- Random number generation (uniform, normal distribution, integers)

### Array Properties & Data Types
- Shape, size, and dimensions of arrays
- Data types (`int32`, `int64`, `float32`, `float64`, `bool_`, `complex128`)
- Type casting with `astype()`
- Understanding type priorities (int < float < string)

### Arithmetic & Aggregation Operations
- Element-wise operations (+, -, *, /, **)
- Aggregation functions: `sum()`, `mean()`, `min()`, `max()`, `std()`, `var()`

### Indexing & Slicing
- 1D and 2D array indexing (positive and negative)
- Slicing with start, end, and step
- Fancy indexing (selecting multiple elements)
- Boolean masking for conditional filtering

### Array Manipulation
- **Reshaping**: `reshape()` - converting between dimensions (view)
- **Flattening**: `ravel()` (view) vs `flatten()` (copy)
- **Modifying**: `insert()`, `append()`, `delete()`
- **Combining**: `concatenate()`, `stack()`, `hstack()`, `vstack()`, `dstack()`
- **Splitting**: `split()`, `hsplit()`, `vsplit()`, `dsplit()`

### Advanced Concepts
- **Broadcasting**: Operations on arrays of different shapes
- **Vectorization**: Applying operations without loops
- **Handling special values**: `nan`, `inf`, `-inf`
- Functions: `isnan()`, `isinf()`, `nan_to_num()`

## 📁 Daily Breakdown

- **day1.py** - NumPy basics, array creation methods, special functions (`arange`, `linspace`, `logspace`, `zeros`, `ones`, `full`, `eye`, `empty`), random number generation
- **day2.py** - Array properties (`shape`, `size`, `ndim`, `dtype`), type casting, arithmetic operations, aggregation functions
- **day3.py** - Indexing (1D & 2D), slicing techniques, fancy indexing, boolean masking, reshaping arrays, `ravel()` vs `flatten()`
- **day4.py** - Array modification methods (file contains code for insert, append, concatenate, delete, stack operations, split operations)
- **day5.py** - Broadcasting rules, vectorization, handling missing/special values (`nan`, `inf`)

## 🔑 Key Takeaways

- **Views vs Copies**: `reshape()` and `ravel()` create views (modify original), while `flatten()` creates a copy
- **Broadcasting**: NumPy automatically expands arrays of different shapes when performing operations
- **Vectorization**: Eliminates the need for Python loops, making code faster and more efficient
- **Data Type Hierarchy**: int < float < string (changes affect entire array)
- **Memory Efficiency**: NumPy arrays are faster and more memory-efficient than Python lists

## 💡 Why NumPy Matters for ML

NumPy is the backbone of ML libraries (Pandas, Scikit-learn, TensorFlow). Understanding array manipulation, broadcasting, and vectorization is crucial for:
- Efficient data preprocessing
- Matrix operations in neural networks
- Feature engineering and transformations
- Mathematical computations in ML algorithms