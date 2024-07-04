### Key Properties and Methods in NumPy

#### Array Creation
- `numpy.array()`: Creates an array.
- `numpy.zeros()`: Creates an array filled with zeros.
- `numpy.ones()`: Creates an array filled with ones.
- `numpy.full()`: Creates an array filled with a specified value.
- `numpy.empty()`: Creates an uninitialized array.
- `numpy.arange()`: Creates an array with a range of values.
- `numpy.linspace()`: Creates an array with linearly spaced values.
- `numpy.eye()`: Creates an identity matrix.

#### Array Attributes
- `ndarray.ndim`: Number of array dimensions.
- `ndarray.shape`: Dimensions of the array.
- `ndarray.size`: Total number of elements.
- `ndarray.dtype`: Data type of the elements.
- `ndarray.itemsize`: Size of each element in bytes.
- `ndarray.nbytes`: Total bytes consumed by the elements.

#### Array Manipulation
- `numpy.reshape()`: Gives a new shape to an array.
- `numpy.flatten()`: Flattens the array.
- `numpy.transpose()`: Transposes the array.
- `numpy.concatenate()`: Joins a sequence of arrays along an existing axis.
- `numpy.split()`: Splits an array into multiple sub-arrays.
- `numpy.stack()`: Stacks arrays along a new axis.

#### Mathematical Functions
- `numpy.add()`, `numpy.subtract()`, `numpy.multiply()`, `numpy.divide()`: Basic arithmetic operations.
- `numpy.exp()`, `numpy.log()`, `numpy.log10()`: Exponential and logarithmic functions.
- `numpy.sin()`, `numpy.cos()`, `numpy.tan()`: Trigonometric functions.
- `numpy.sqrt()`: Square root.
- `numpy.power()`: Element-wise power.

#### Statistical Functions
- `numpy.mean()`: Arithmetic mean.
- `numpy.median()`: Median.
- `numpy.std()`: Standard deviation.
- `numpy.var()`: Variance.
- `numpy.min()`, `numpy.max()`: Minimum and maximum values.
- `numpy.percentile()`: Percentile.

#### Linear Algebra
- `numpy.dot()`: Dot product.
- `numpy.cross()`: Cross product.
- `numpy.vdot()`: Dot product of vectors.
- `numpy.inner()`: Inner product.
- `numpy.outer()`: Outer product.
- `numpy.linalg.det()`: Determinant.
- `numpy.linalg.inv()`: Inverse of a matrix.
- `numpy.linalg.eig()`: Eigenvalues and eigenvectors.

#### Random Sampling
- `numpy.random.rand()`: Generates an array of given shape with random samples from a uniform distribution over `[0, 1)`.
- `numpy.random.randn()`: Generates an array with samples from the standard normal distribution.
- `numpy.random.randint()`: Generates random integers.
- `numpy.random.choice()`: Generates a random sample from a given 1-D array.

This summary includes some of the most frequently used methods and properties. For a comprehensive list, it's best to refer to the [official NumPy documentation](https://numpy.org/doc/stable/reference/).