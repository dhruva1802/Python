# Databricks notebook source
# MAGIC %md
# MAGIC Equal to operatior ==

# COMMAND ----------

33 == 44

# COMMAND ----------

33 == 33

# COMMAND ----------

10 != 20

# COMMAND ----------

10 < 20

# COMMAND ----------

10 > 20

# COMMAND ----------

10 != 15

# COMMAND ----------

# MAGIC %md
# MAGIC logical operatior

# COMMAND ----------

# and
10 < 20 and 20 <30

# COMMAND ----------

10 > 20  and 20 >30 # if both condition is true than only get true else false

# COMMAND ----------

10 > 20 or 20 > 30 ## if any one condition is true than only get true else false

# COMMAND ----------

10 > 20 or 50 > 40

# COMMAND ----------

# MAGIC %md
# MAGIC enumerate
# MAGIC
# MAGIC Enumerate is very useful function to use with for loops.
# MAGIC
# MAGIC Enumerate() method adds a cocunter to an iterable and return it in a form of enumerate object.
# MAGIC
# MAGIC This enumerate object can then be used directly in gor loops or be converted into a list of tuple using list method().

# COMMAND ----------

for i , letter in enumerate ('dhruva'):
  print(f"at index {i}:the letter {letter}")

# COMMAND ----------

# MAGIC %md
# MAGIC sorted list()
# MAGIC
# MAGIC The sorted() function return z sorted list of the speified iterable object.
# MAGIC
# MAGIC sorted(iterable, key=key, reverse=reverse)

# COMMAND ----------

a=("c","b","a","d","e","f")
x=sorted(a) # sort like a- z
print(x)

# COMMAND ----------

a=("c","b","a","d","e","f")
x=sorted(a,reverse=True) # sort like z-a
print(x)


# COMMAND ----------

# MAGIC %md
# MAGIC globals()
# MAGIC
# MAGIC The global() function return the global syambol table as a dict. key value pair data of all object

# COMMAND ----------

var=globals
print(var)

# COMMAND ----------

loc=locals()
print(loc)

# COMMAND ----------

# MAGIC %md
# MAGIC len()
# MAGIC
# MAGIC len() function will give length of object or no of items in object.

# COMMAND ----------

# print len of int data type
list_a=[1,2,3,4,5]
print('no of items:',len(list_a))

# COMMAND ----------

# print len of char data type
char_a=['a','b','c','d','e']
print('no of items:',len(char_a))

# COMMAND ----------

# MAGIC %md
# MAGIC Random
# MAGIC
# MAGIC python comes with a built in library. There are a lot of function  in this random libraty, so we will only two useful functions for now.

# COMMAND ----------

from random import shuffle
list_a=[1,2,3,4]
shuffle(list_a)
print(list_a)

# COMMAND ----------

from random import randint
randint(0,100)

# COMMAND ----------

from random import randint
randint(1,100)


# COMMAND ----------

# MAGIC %md
# MAGIC split: are used to split the string
# MAGIC

# COMMAND ----------

email="dhruvdaware1802@gmail.com"
output=email.split('@')
print(output)

# COMMAND ----------

string=" this is my car"
output=string.split("is")
output

# COMMAND ----------

# MAGIC %md
# MAGIC upper and lowwer are used ot conver char or string

# COMMAND ----------

name="dhruv"
name.upper()

# COMMAND ----------

name='DHRUA'
name.lower()

# COMMAND ----------

# MAGIC %md
# MAGIC replace(from,to)
# MAGIC
# MAGIC replace char by char using replace() function

# COMMAND ----------

string="Databricks Traning"
string=string.replace('Databricks')