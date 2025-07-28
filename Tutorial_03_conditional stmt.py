# Databricks notebook source
# MAGIC %md
# MAGIC If stmt:

# COMMAND ----------

Var1=55;
if Var1 > 55:
  print("True")
else :
  print("false")

# COMMAND ----------

a=30
b=20
if a > 20:
    print("a is greather than b");
else :
    print("b is greather than a");
   

# COMMAND ----------

# MAGIC %md
# MAGIC If-elif

# COMMAND ----------

x=10
y=10
if x < y:
  print('print x is less than y')
elif x > y:
  print('print x is greather than y')
else :
  print(' x and y are same')

# COMMAND ----------

a=100
if a == 200:
    print("a value is 200")
elif a>200:
    print("a value is greater than 200")
elif a <200:
    print("a value is less than 200")
else:
    print("a value is not available")

# COMMAND ----------

# MAGIC %md
# MAGIC Short hand if...else
# MAGIC
# MAGIC If you have only one stmt to exectue one for if and one for else, you can put it all on same line.

# COMMAND ----------

a=300;
b=400;
if a < b: print("a is less than b")

# COMMAND ----------

a=700
b=550
print(" a is greather than b",a) if a > b else print(' a is lessthan than b')

# COMMAND ----------

