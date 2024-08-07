#the array object in numpy is called ndarray

import numpy as np
#! The quick brown

#* 0D Array
a=np.array(18)
print("0D Array")
print(a.ndim)

#* 1D Array
x=np.array([1,2,3,4,5,6])
print(x)
print(type(x))
print(x.ndim)

#* 2D Array
y=np.array([[1,2,3],[4,5,6]])
print("2D Array")
print(y)
print(y.ndim)

#*3D Array
z=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print("3D Array")
print(z)
print(z.size)
print(z.ndim)

#! using ndmin function we can create X-D array 
b=np.array([1,2,3,4],ndmin=6)
print(b)
print(b.size)
print(b.ndim)

#* ndmin is used to create multidimension array
#* ndim is used to check the dimesion of an array