# Databricks notebook source
# MAGIC %md
# MAGIC Python Exception Handling handles errors that occur during the execution of a program. Exception handling allows to respond to the error, instead of crashing the running program. It enables you to catch and manage errors, making your code more robust and user-friendly.
# MAGIC
# MAGIC Difference Between Exception and Error
# MAGIC
# MAGIC Error: Errors are serious issues that a program should not try to handle. They are usually problems in the code's logic or configuration and need to be fixed by the programmer. Examples include syntax errors and memory errors.
# MAGIC
# MAGIC Exception: Exceptions are less severe than errors and can be handled by the program. They occur due to situations like invalid input, missing files or network issues.

# COMMAND ----------

# MAGIC %md
# MAGIC Handling expections
# MAGIC
# MAGIC it is possiable to write program that handle seleted exceptions.
# MAGIC
# MAGIC Try block
# MAGIC
# MAGIC here we can write our code ==main execution code we can write in try bloak
# MAGIC
# MAGIC exception
# MAGIC
# MAGIC here we can handle whichever exception or error throwing by try block

# COMMAND ----------

try:
  a=55
  b=0
  c=a/b
except:
  print("exception blob")

# COMMAND ----------

# we also give exception name to except fun
try:
    a=55
    b=0
    c=a/b
except ZeroDivisionError as e:
    print("exception blob:",e)

# COMMAND ----------

try:
    a=55
    b=10
    c=a/b
    print('try block:',c)
except ZeroDivisionError as e:
    print('exception block error msg:',E)

# COMMAND ----------

def divibyzero(x,y):
    try:
        return x/y
    except ZeroDivisionError as e:
        print('exception block error msg:',e)
        return None
divibyzero(10,5)

# COMMAND ----------

def divibyzero(x,y):
    try:
        return x/y
    except ZeroDivisionError as e:
        print('exception block error msg:',e)
    except:
        print("the exception error msg")
divibyzero(5,0)
divibyzero(5,'2')

# COMMAND ----------

divibyzero(10,1)

# COMMAND ----------

# MAGIC %md
# MAGIC