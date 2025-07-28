# Databricks notebook source
import numpy as np

# COMMAND ----------

# Creating Numpy 1Darray
x=np.array([1,2,3,4,5])
print(x)
print(type(x)) 

# COMMAND ----------

# creating 2D array
y=np.array([[1,2,3],[4,5,6]])
print(y)
print(type(y))

# COMMAND ----------

# creating 3 D array
z=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(z)
print(type(z))

# COMMAND ----------

# MAGIC %md
# MAGIC Numpy provides: covenient methods to create array intialized with specific values like zeros and ones.

# COMMAND ----------

# creating np array with zeros
a1_zeros=np.zeros((2,3,)) # 2 is row and 3 is col
print(a1_zeros)
print(type(a1_zeros))

# COMMAND ----------

# Creating np array with ones
a1_ones=np.ones((2,3))
print(a1_ones)
print(type(a1_ones))

# COMMAND ----------

# creating array with arange
a1_arange=np.arange(0,10,2)
print(a1_arange)

# COMMAND ----------

# MAGIC %md
# MAGIC Numpy array indexing: used to access element of an array using indices.

# COMMAND ----------

arr1d=np.array([1,2,3,4,5,6])

# single element accdess
print('single element access:',[arr1d[2]])

# Negative indexing
print('Negative indexing:',[arr1d[-1]])

# Create a 2D index
arr2d=np.array([[1,2,3],[4,5,6]])

# accessing 2d array
print('2d array access:',arr2d[0,2])

# COMMAND ----------

array=np.array([[1,2,3],[4,5,6]])
array[1,2]

# COMMAND ----------

# slicing 1d the index
arr=np.array((1,2,3,4,5,6))
arr[1:4]



# COMMAND ----------

# slicing 2d array
arr=np.array([[1,2,3],[4,5,6]])
print('range of elemnts:',arr[1:4])

# COMMAND ----------

arr=np.array([[1,2,3],[4,5,6]])
# elemts from index 1 to 3
print('range of elemets:',arr[1:4])

# all rows, second column
print("Multidimensional slicing:",arr[:,1])

# COMMAND ----------

arr=np.array([10,20,30,40,50,60])

# Integer array indexing
indices=np.array([1,3,5])
print("integer array indexing:",arr[indices])

# boolean array indexing

cond=arr > 20
print("\n Elements greater than 20:",arr[cond])

# COMMAND ----------

# basic numpy operations

x=np.array([1,2,3])
y=np.array([4,5,6])

# addition
add=x+y
print('addition:',add)

# subtraction
sub=x-y
print('subtraction:',sub)

# multiplication
mul=x*y
print('multiplication:',sub)

# Div
div=x/y
print('division:',div)

# COMMAND ----------

arr=np.array([-3,-2,-1,0,1,2,3])

# Applying a unary operation: absolute value
result=np.absolute(arr)
print('Absolute value:',result)

# COMMAND ----------

# Two example array 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

# Applying a binary operations: addition
result=np.add(arr1,arr2)

print('Array 1:',arr1)
print('Array 2:',arr2)
print('Addition:',result)

# COMMAND ----------

# create an array of sine values
a=np.array([0,np.pi/2,np.pi])
print('sine values of array elements:',np.sin(a))

# exp values
a=np.array([0,1,2,3,4])
print('exponent of array elements:',np.exp(a))

# square root of array value
print('square root of array elements:',np.sqrt(a))


# COMMAND ----------

# create array and sort it
import numpy as np
dtypes=[('name','S10'),('grand_year',int),('CGPA',float)]

# value to put in array
values=[('Ram',2009,8.5),('Sita',2012,9.0),( 'Laxman',2008,7.5)]

# creating array
arr=np.array(values,dtype=dtypes)
print("\n Array sorted by names:\n",
      np.sort(arr,order='name'))

print('Array sorted by graducation year and cgpe:\n',
      np.sort(arr,order=['grand_year','CGPA']))

# COMMAND ----------

# MAGIC %md
# MAGIC creating array by different way

# COMMAND ----------

import numpy as np

# creating a rank 1 array
arr=np.array([1,2,3,4])
print(arr)
print(type(arr))

# COMMAND ----------

# creating array with 2D array
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(type(arr))

# COMMAND ----------

# creating array with tuple
arr=np.array((1,2,3))
print(arr)
print(type(arr))

# COMMAND ----------

# MAGIC %md
# MAGIC Accessing the array

# COMMAND ----------

arr=np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])
arr2=arr[:2,::2]

# COMMAND ----------

# MAGIC %md
# MAGIC basic array operations

# COMMAND ----------

a=np.array([[1,2],[3,4]])

# defining array 2
b=np.array([[4,3],[2,1]])

# adding 1 to every element
print('Adding 1 to every element:',a+1)

# COMMAND ----------

import numpy as np
a=np.array([1,2,3,4,5])
a

# COMMAND ----------

# list and array size comparision
# array take less size as compair to list
import sys
i=range(1000)
print(sys.getsizeof(5)*len(i))
# numpy array
a=np.arange(1000)
print(a.size*a.itemsize)


# COMMAND ----------

# array is fast as compair to list
import timeit
import numpy as np

l1 = range(10000)
l2 = range(10000)
a = np.arange(10000)
b = np.arange(10000)

print(timeit.timeit(stmt='[x+y for x,y in zip(l1,l2)]', number=10000, globals=globals()))
print(timeit.timeit(stmt='a+b', number=10000, globals=globals()))

l1 = range(10000)
l2 = range(10000)
a = np.arange(10000)
b = np.arange(10000)

print(timeit.timeit(stmt='[x+y for x,y in zip(l1,l2)]', number=10000, globals=globals()))
print(timeit.timeit(stmt='a+b', number=10000, globals=globals()))

# COMMAND ----------

# create array and cheke dim of taht array
a=np.array([[1,2],[3,4],[5,6]])
print(a.ndim)

# COMMAND ----------

b=np.array([1,2,3])
print(b.ndim)

# COMMAND ----------

# create array i t and convert it into float
a=np.array([[1,2],[3,4],[5,6]],dtype=float)
print(a)

# COMMAND ----------

# create array cheke it is size and shape and dim
a=np.array([1,2,3,4,5,6,7])
print(a.size)
print(a.shape)
print(a.ndim)

# COMMAND ----------

# create array from 1 to 10 with 2 step
a=np.arange(1,10,2)
print(a)

# COMMAND ----------

# create 20 array from 1 to 10
b=np.linspace(1,10,20)
print(b)

# COMMAND ----------

# create array and reshape it
a=np.arange(1,10)
print(a)
print(a.reshape(3,3))

# COMMAND ----------

# create multi dim array and ravel it into 1 dim
a=np.array([[1,2],[3,4],[5,6]])
print(a.ravel())

# COMMAND ----------

# create array and perform operations
a=np.array([[1,2],[3,4],[5,6]])
a.min()
a.max()
a.sum()

# COMMAND ----------

# create array and sum of first col
a=np.array([[1,2],[3,4],[5,6]])
a.sum(axis=0)

# COMMAND ----------

a=[1,2,3,4]
b=[3,4,5,5]
a+b
a=np.array([1,2,3,4])
b=np.array([3,4,5,5])
a+b

# COMMAND ----------

# slicing the array
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

# COMMAND ----------

a[2,2]

# COMMAND ----------

# spliting the array
# splitting the array
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.hsplit(a, 3)

# COMMAND ----------

# MAGIC %md
# MAGIC