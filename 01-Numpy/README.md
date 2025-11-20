# Module 01: NumPy

NumPy is the core numerical computing library in Python. It provides fast, vectorized operations and forms the foundation of Pandas, SciPy, and most ML frameworks.

## Topics Covered

### Array Creation and Initialization
- Manual and range-based creation  
- `arange()`, `linspace()`, `logspace()`  
- `zeros()`, `ones()`, `full()`, `eye()`, `empty()`  
- Random generation (uniform, normal, integers)

### Array Properties and Data Types
- Shape, size, dimensions  
- NumPy numeric and boolean dtypes  
- Casting with `astype()`  
- Type promotion rules

### Arithmetic and Aggregation
- Element-wise mathematical operations  
- Aggregation functions: `sum`, `mean`, `min`, `max`, `std`, `var`

### Indexing and Slicing
- 1D and 2D indexing  
- Slicing with custom step  
- Fancy indexing  
- Boolean masking for conditional filtering

### Array Manipulation
- Reshaping (`reshape`)  
- Flattening (`ravel` vs `flatten`)  
- Structural modification: `insert`, `append`, `delete`  
- Combining arrays: `concatenate`, `stack`, `hstack`, `vstack`, `dstack`  
- Splitting: `split`, `hsplit`, `vsplit`, `dsplit`

### Advanced Concepts
- Broadcasting rules  
- Vectorization (loop-free operations)  
- Handling special values (`nan`, `inf`, `-inf`)  
- Functions: `isnan`, `isinf`, `nan_to_num`

## Notebook Breakdown

- **01_array_creation_initialization.ipynb**  
  Covers array creation, special constructors, ranges, and random sampling.

- **02_properties_dtypes_operations.ipynb**  
  Discusses array properties, data types, type casting, arithmetic, and aggregations.

- **03_indexing_slicing_reshaping.ipynb**  
  Covers indexing (1D/2D), slicing, fancy indexing, masking, reshaping, flattening.

- **04_array_modification.ipynb**  
  Focuses on modification and combination operations (insert, append, concatenate, delete, stacking, splitting).

- **05_broadcasting_vectorization_missing_values.ipynb**  
  Covers broadcasting rules, vectorization, and handling of missing or special values.

## Key Takeaways
- `reshape` and `ravel` return views; `flatten` returns a copy.  
- Broadcasting enables arithmetic across compatible shapes.  
- Vectorization is significantly faster than Python loops.  
- NumPy arrays enforce efficient dtypes and are memory-efficient versus lists.

## Why NumPy Matters for Machine Learning
NumPy underpins data preprocessing, matrix algebra, feature engineering, and the computational core of modern ML libraries. Mastery of NumPy is mandatory before moving into Pandas, Scikit-Learn, or deep learning frameworks.