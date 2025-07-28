# Databricks notebook source
# Datatype in python
# range: The reange() function is used to generate a sequences of number over a time.
# syantax: range(start,stop,end)

# COMMAND ----------

v_range=range(10) # stop,step are optional
print(v_range)
print(type(v_range))

# COMMAND ----------

# range with start stop and step
v_range=(1,10,2)
print(v_range)

# COMMAND ----------

v_range=range(10)
list(v_range)

# COMMAND ----------

# string: 
Name='Dhruv'
print(Name)
print(type(Name))

# COMMAND ----------

Name="10" # any thing we can print inside "" consider as string
print(Name)
print(type(Name))

# COMMAND ----------

Name='''Dhruv
Daware'''
print(Name)
print(type(Name))


# COMMAND ----------

# indexing in string
Name="Dhruv"
Name[3]

# COMMAND ----------

# int
Roll_no=20;
print(Roll_no)
print(type(Roll_no))

# COMMAND ----------

# float
Name=3.14;
print(Name)
print(type(Name))

# COMMAND ----------

# MAGIC %md
# MAGIC List[]
# MAGIC
# MAGIC List is collection of data type which ordered and changeable (Mutable). allow duplicate value
# MAGIC
# MAGIC

# COMMAND ----------

My_list=[1,2,3,'Dhruv',3.14]
print(My_list)
print(type(My_list))

# COMMAND ----------

My_list=[1,2,3,3.14,'Dhruv']
My_list[2]  # indexing in list

# COMMAND ----------

# adding two list
My_list1=[1,2,3]
My_list2=[4,5,6]
My_list1+My_list2

# COMMAND ----------

# adding element in list
My_list=[1,2,3]
My_list.append(4)
print(My_list)

# COMMAND ----------

# MAGIC %md
# MAGIC Tuple()
# MAGIC
# MAGIC Tuple is a collection datatype which is ordered and unchageable. allow duplicate value.

# COMMAND ----------

a_tuple=(1,2,3)
print(a_tuple)
print(type(a_tuple))

# COMMAND ----------

a_tuple=(1,2,3.14,'Dhruv')
print(a_tuple)
print(type(a_tuple))

# COMMAND ----------

tuple1=(1,2,3)
tuple1.append(2)

# COMMAND ----------

# MAGIC %md
# MAGIC Set{}
# MAGIC
# MAGIC A set is collection which is unordered and unindexed. No duplicate value allowed. it is mmutable

# COMMAND ----------

My_set={1,2,3,3.15}
print(My_set)


# COMMAND ----------

# adding element in set
My_set={1,2,3}
My_set.add(4)
print()

# COMMAND ----------


My_set={1,2,3,3}
print(My_set) # set doed not allow duplicate value

# COMMAND ----------

# MAGIC %md
# MAGIC Dict:{}
# MAGIC
# MAGIC Dict is collection of key value pair. and it allow duplicate value. it is mmstable

# COMMAND ----------

My_dict={"Name":['Ram','Geeta','Seeta'],"Roll_No":[1,2,3]}
print(My_dict)
print(type(My_dict))

# COMMAND ----------



# COMMAND ----------

My_dict["Name"].append('Shyam')
display(My_dict)
My_dict[Roll_No].append(21)
Print(My_dict)

# COMMAND ----------

# indexing on dict
My_dict2=My_dict["Name"][2]
print(My_dict2)

# COMMAND ----------

# dict with single value and single column
dict1={"Name":"ram","age":20}
print(dict1)

# COMMAND ----------

# MAGIC %md
# MAGIC frozenset()
# MAGIC
# MAGIC The frozenset() is an inbuilt function is python whcih takses an iterable object as input and make them immutable. simply it freeze the iterable object and make them unchangeable.

# COMMAND ----------

x=frozenset({1,2,3,3})
print(x)
print(type(x))

# COMMAND ----------

# MAGIC %md
# MAGIC Bool
# MAGIC
# MAGIC The boolean data type is either true or false. in python boolean variable are defined by thre and false keyword.

# COMMAND ----------

a=False
b=True
print('variable a is type:',type(a))
print('Variable b is type:',type(b))

# COMMAND ----------

# typecasting of bool
num=1
bool(num)
print(bool(num))
print(type(bool(num)))

# COMMAND ----------

# MAGIC %md
# MAGIC bytes data type(): it is immutable

# COMMAND ----------

#byte of string
x=b"Hello"
print('Bytes Data type:',type(x))
print(x)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC

# COMMAND ----------

# byte of int
v_int=55
print(bytes(v_int))

# COMMAND ----------

# MAGIC %md
# MAGIC # bytearray()
# MAGIC
# MAGIC Bytearray() method return a bytearray object which is an array of given bytes. it gives a mutable sequences in integer in the range 0 <= x < 256

# COMMAND ----------

# converting int into bytearray
x=bytearray([14])
print('Byte Array Data type:',type(x))
print(x)

# COMMAND ----------

# converting int into bytaarray
x=bytearray(144)
print('Byte Array Data type:',type(x))
print(x)

# COMMAND ----------

# MAGIC %md
# MAGIC Memoryview()
# MAGIC
# MAGIC Memory views can be accessed using indexing and slicing, similar to sequences like lists or strings. Indexing returns the byte value at the specified position as an integer, while slicing returns a new memory view representing the specified range of bytes. This approach is particularly useful for reading specific sections of large datasets without copying the entire data into memory, which improves efficiency.
# MAGIC
# MAGIC  

# COMMAND ----------

data=b'Python'
mv=memoryview(data)
print(mv)
print(type(mv))

# COMMAND ----------

# creating a memory view from bytes
data=b'Python'
mv=memoryview(data)

# accessing indivisual byte using indexing
print(mv[0])

# accessig a range of bytes using slicing
print(mv[1:4].tobytes())

# COMMAND ----------

# creating a bytearray for mutable data
arr=bytearray(b'abcde')
mv=memoryview(arr)

# modifying a byte using indexing
mv[0]=65
print(arr)