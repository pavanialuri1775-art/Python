#Python NumPy
#it is a python library used to perform fast numerical calculations work with arrays.
#Numpy provides effecient numerical computing with
#Array manipulation:Create and reshape arrays
#Mathematical functions:performs operatoions like add,multiply
#Linear algebra:matrix operations
#random number generation:generates random data.

#Arrays in Numpy:A NumPy array is a structured collection of elements of the same data type stored in a table format.
#The number of dimensions is called the rank and the size along each dimension is called the shape.
#In NumPy, arrays are called ndarray and elements are accessed using square brackets [].
import numpy as np
arr=np.array([1,2,3])
print(arr)
arr = np.array([[1, 2, 3],[4, 5, 6]])
print(arr)
arr = np.array((1, 3, 2))
print(arr)