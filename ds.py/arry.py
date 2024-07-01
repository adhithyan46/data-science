# import numpy as np
# arr=np.array([1,2,3,4])
# print(arr)
# print(type(arr))

import numpy as np
arr2=np.array([[1,2],[3,4]])
arr3=np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(arr2)
print(arr3)
print(arr3.ndim)
print(arr2.ndim)

import numpy as np
arr=np.array([[1,2],[3,4]])
arr
arr[0,1]

import numpy as np 
arr=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr
arr[1,0,0]

#slicing

import numpy as np
arr=np.array([1,2,3,4,5,6])
arr[1:5]

import numpy as np
arr=np.array([1,2,3,4,5,6])
arr[5:]

import numpy as np
arr=np.array([1,2,3,4,5,6])
arr[-4:-2]

import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr[1,0:2]

import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr[0:2,1:5]

import numpy as np
arr=np.array([[1,2,3,4,5,6]])
arr[::2]

import numpy as np
arr=np.array([[1,2,3,4,5,6]])
arr[0:5:2]

#datatype

import numpy as np
arr=np.array([1,2,3,4])
arr.dtype

import numpy as np
arr=np.array(['adhi','babu','shibu'])
arr.dtype

import numpy as np
arr=np.array([1,2,3,4],dtype='S')
arr
arr.dtype

import numpy as np
arr=np.array([1,2,3,4],dtype='i4')
arr
arr.dtype

import numpy as np
arr=np.array([1,2,3,4])
narr=arr.astype('S')
narr
narr.dtype

import numpy as np
arr=np.array([1,2,3,4])
narr=arr.astype('bool')
narr


##copy

import numpy as np
arr=np.array([1,2,3,4])
x=arr.copy()
arr[3]=50
print('copy=',x)
print('og=',arr)

##view

import numpy as np 
arr=np.array([1,2,3,4])
x=arr.view()
arr[2]=50
print('copy=',x)
print('og=',arr)

##base

import numpy as np
arr=np.array([1,2,3,4])
x=arr.copy()
y=arr.view()
print(x.base)
print(y.base)

##shape

import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr.shape



import numpy as np
arr=np.array([1,2,3,4,5,6],ndmin=3)
arr
arr.shape

##reshape

import numpy as np
arr=np.array([1,2,3,4,5,6])
n_arr=arr.reshape(2,3)
n_arr

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
n_arr=arr.reshape(2,5,1)
n_arr
