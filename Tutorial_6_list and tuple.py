# Databricks notebook source
# MAGIC %md
# MAGIC Python Datastastructure or collection (Arrays)
# MAGIC
# MAGIC There are four collection data type in python programing language.
# MAGIC
# MAGIC 1) List is collection which ordered and changeble. aloow duplicate value.
# MAGIC
# MAGIC 2) Tuple is collection which ordered and unchangeble. allows duplicate value
# MAGIC
# MAGIC 3) set is collection whcih unordered and unidexed. no duplicate value allow.
# MAGIC
# MAGIC 4) Dict is a collection which is unorderd, chageable and indexed. No duplicate member allow.

# COMMAND ----------

# List[]
My_list=[1,2,3,4,5,6,5] # it allow duplicate value
print(My_list)
type(My_list)

# COMMAND ----------

# list with range
my_list=list(range(1,10))
my_list

# COMMAND ----------

# list diffeent data type
my_list=[1,2,3,'Dhruv',31.04]
my_list


# COMMAND ----------

# indexing in list
my_list=list(range(1,20))
my_list[1]  # postive index left to right
my_list[-1] # negative index right to left

# COMMAND ----------

list=['raj','seeta','geeta','janu']
list[2]

# COMMAND ----------

# MAGIC %md
# MAGIC Ranges of indexes
# MAGIC
# MAGIC List can be indexed and sliced
# MAGIC
# MAGIC You can specify a range of indexes by specifying where to start and wherre to end the range. it return value will new list with specified items.

# COMMAND ----------

my_list=["apple","banana","orange","kiwi","melon","mango"]
my_list[0:3]

# COMMAND ----------

list=[1,2,3,4,5,6,7,8,9,10]
list[1:8:2]  # indexing with step

# COMMAND ----------

# MAGIC %md
# MAGIC Append: always add value at end of list
# MAGIC
# MAGIC insert: add value using index position

# COMMAND ----------

# addig element in existing list
my_list=[1,2,3,4,5]
my_list.append(6)
my_list

# COMMAND ----------

# adding element in list at specific index
my_list=[1,2,3,4,5,6,7]
my_list.insert(0,2)  # insert 2 at index 0
my_list

# COMMAND ----------

# slicing :[min:max(n-1)]
my_list=[1,2,3,4,5,6,7,8,9]
my_list[-5:-1]

# COMMAND ----------

# create list and update value at speicif index
month_list=['Jan','Feb','March','April','May','June','Aug']
month_list[6] = 'July'
month_list

# COMMAND ----------

# inserting list into another list
num=[1,2,3,4]
num.append([5,6])
num

# COMMAND ----------

# create list and print len of list
num=[1,2,3,4,5]
len(num)

# COMMAND ----------

# create list find len after inseritng and before inseritng
num=[1,2,3,4]
print("before inseritn:",num)
num.insert(len(num),5)
print("after inseritng:",num)

# COMMAND ----------

# MAGIC %md
# MAGIC Extend: It take a list as a argument and append all of the elements.

# COMMAND ----------

mylist=['jan','feb','march']
monthlist=['april','may']
mylist.extend(monthlist)
mylist

# COMMAND ----------

# create list and find len and sort it 
mylist=[1,2,3,4,5]
len(mylist)
mylist.sort() # by default sort in asc order
my_list

# COMMAND ----------

# sort list into descending order
mylist=[1,2,3,4,5]
mylist.sort(reverse=True)
mylist

# COMMAND ----------

# MAGIC %md
# MAGIC Remove: used remove element from speicifc index.
# MAGIC
# MAGIC pop: used to remove element from last position.

# COMMAND ----------

# create list and remove elemnt from list
mylist=[1,2,3,4,5]
mylist.remove(3)
mylist

# COMMAND ----------

# create list and pop elemnt from list
mylist=[1,2,3,4]
mylist.pop()
mylist

# COMMAND ----------

# del used to delete value from list
mylist=[1,2,3]
del mylist[1]
print(mylist)


# COMMAND ----------

# create list and cleat it
mylist=[1,2,3,4]
mylist.clear()
mylist

# COMMAND ----------

# MAGIC %md
# MAGIC COPY:
# MAGIC
# MAGIC You cannot copy a list simply by typing liat2=list1. because list2 will only be a references to list1 and chages made in list1 will automatically also be made in list2.
# MAGIC
# MAGIC There are ways to make a copy. one way it to use built in list method copy.

# COMMAND ----------

thislist=["apple","banana","cherry"]
copylist=thislist # copy thislist into copylist
thislist.append("orange")
print(thislist)
print(copylist)

# COMMAND ----------

# if you want copy one list into another but if modify first list another list not update then we .copy()
thislist=["apple","banana","cherry"]
copylist=thislist.copy() # copy thislist into copylist
thislist.append("orange")
print(thislist)
print(copylist)

# COMMAND ----------

# create list and find index of specific value
vowels=['a','e','i','o','u']
index=vowels.index('i')
print(index)

# COMMAND ----------

# if we have duplicate value in list then how to find index 
vowels=['a','e','i','o','u','e','e']
print('index of e is:', vowels.index('e'))
print('index of 2nd e:',vowels.index('e',2)) # 2 is second value of e
print('index of 3rd e:',vowels.index('e',6))


# COMMAND ----------

# MAGIC %md
# MAGIC Tuple:
# MAGIC
# MAGIC once we can created tuple than we can not change tuple.
# MAGIC but we can convert tuple into list than we chage.

# COMMAND ----------

my_tuple=(1,2,3,4)
type(my_tuple)

# COMMAND ----------

my_tuple=(1,2,3,4)
len(my_tuple)

# COMMAND ----------

my_tuple=(1,2,3,4)
my_tuple[2]