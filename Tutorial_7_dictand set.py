# Databricks notebook source
# MAGIC %md
# MAGIC Set:
# MAGIC it does not store duplicate value. and it is mustable.
# MAGIC
# MAGIC set is collection which is unordered and unidexed. no duplicate value are allowed

# COMMAND ----------

my_set={1,2,3,4}
type(my_set)

# COMMAND ----------

# set with different datatype
my_set={1,2,3,'dhruvb',3.14}
print(my_set)
type(my_set)

# COMMAND ----------

# create set that auto remove deuplicate value
my_set={1,2,3,4,1} # 1 is duplicate
print(my_set)

# COMMAND ----------

my_set={1,2,3,'a','b','c',4,5}
print(my_set)

# COMMAND ----------

# MAGIC %md
# MAGIC index and slicing not allow in set so we used for loop for accessing items.
# MAGIC
# MAGIC you cannot access items in a set by referring to an index or a key.
# MAGIC
# MAGIC but using loopmwe canaccess it

# COMMAND ----------

thisset={'a','b','c','d','e','f','g','h'}
for x in thisset:
  print(x)

# COMMAND ----------

# adding element in set
thisset={'a','b','c','d','e','f','g','h'}
thisset.add('i')
print(thisset)

# COMMAND ----------

# adding multiple value in set using update
thisset={'a','b','c','d','e','f','g','h'}
thisset.update(['i', 'j'])
print(thisset)

# COMMAND ----------

# MAGIC %md
# MAGIC to remove item for set we used remove or discard

# COMMAND ----------

thiset={'apple','banana','cat','dog'}
thiset.remove('apple')
print(thiset)

# COMMAND ----------

# Removing more one elemnt from set
thiset={'apple','bat','cat','dof'}
thiset -= {'bat','cat'}
print(thiset)

# COMMAND ----------

list_a=[1,2,3,4]
list_a.append(5)
list_a.append(6)
print('before delection:',list_a)
list_a.pop()
print('after delection:',list_a)
list_a.pop()
print('aftet deletion:',list_a)

# COMMAND ----------

# removeing element base on index value
my_set={1,2,3,4,5}
my_set.remove(2)
my_set

# COMMAND ----------

# MAGIC %md
# MAGIC join two set
# MAGIC there are serveral way to join two or more set in python.
# MAGIC
# MAGIC we can used the union() method that return a new set containing all item from both sets.
# MAGIC
# MAGIC update() method that insert all items from one set into another.

# COMMAND ----------

set1={'a','b',1,2,3}
set2={'c','d',4,5,6}
set2.union(set1)


# COMMAND ----------

# union automatically remove duplicate value
set1={'a','b','c','d',1,2,3}
set2={'c','d',4,5,6,1}
set2.union(set1)

# COMMAND ----------

set1={'a','b','c','d',1,2,3}
set2={'c','d',4,5,6,1}
set2.update(set1)

# COMMAND ----------

# intersection only give comman elemt from both set
set1={1,2,3}
set2={2,3,4}
set1.intersection(set2)

# COMMAND ----------

# create 2 set and print differences bet them
set1={1,2,3}
set2={2,3,4}
set1.difference(set2)

# COMMAND ----------

# create set and copy elemt into another set
set1={1,2,3,4,5}
set2=set1.copy()
print(set2)

# COMMAND ----------

# MAGIC %md
# MAGIC Dict{}:
# MAGIC
# MAGIC A dict is collection which is unordered, chageable and indexed. in python dict are written with curly brckets and they have keys and values

# COMMAND ----------

dict={"key1":"value1","key2":"value2"}
dict

# COMMAND ----------

dict.items()

# COMMAND ----------

dict={'name':"ravi",'age':35}
print(dict)

# COMMAND ----------

for k,v in dict.items():
    print(k,v)

# COMMAND ----------

thisdict={"brand":"ford","model":"mustang","year":1964}
thisdict["year"]

# COMMAND ----------

# updating value in dict
thisdict={"brand":"ford","model":"mustang","year":1964}
thisdict["year"]=2024
thisdict

# COMMAND ----------

# addig key key and value in dict
thisdict={"brand":"ford","model":"mustang","year":1964}
thisdict["colour"]="black"
thisdict

# COMMAND ----------

# removing element from dict
thisdict={"brand":"ford","model":"mustang","year":1964}
thisdict.pop("year")
thisdict

# COMMAND ----------

# popitem pop last insert value from dict
thisdict={"brand":"ford","model":"mustang","year":1964}
thisdict.popitem()
thisdict

# COMMAND ----------

#n dict all item from dict
thisdict={"brand":"ford","model":"mustang","year":1964}
del (thisdict)


# COMMAND ----------

thisdict={"brand":"ford","model":"mustang","year":1964}
thisdict.clear()

# COMMAND ----------

