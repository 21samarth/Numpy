import numpy as np
l1 = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]
arr = np.array(l1)
print(arr)
print(arr.ndim) #?Returns the number of dimansions in array either it is 1D 2D or any multidimansional array
print(arr.shape) #? returns the dimansions of array rows,colums
print(arr.size) #? returns the total number of elements in array
print(arr.dtype) #? returns the data type of array
print(arr.itemsize) #? returns the size of each element in bytes
print(arr.nbytes) #? returns the total size consumed by the array in bytes
