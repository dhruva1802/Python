# Databricks notebook source
# MAGIC %md
# MAGIC Python loops
# MAGIC
# MAGIC The two types of loops discssed were for loops and while loops. For loops and while loops are two structure in python

# COMMAND ----------

# MAGIC %md
# MAGIC For loop with range(): depend on data
# MAGIC
# MAGIC Another method to print the same stmt three times is to use for for loop.
# MAGIC
# MAGIC A for loop is programming structure where a user defined block of code run a specified number of times.
# MAGIC
# MAGIC The bascic structure of a for loop in python s below:
# MAGIC
# MAGIC for var in range(num):

# COMMAND ----------

v_range=range(10)
for a in v_range:
  print(a)

# COMMAND ----------

name="Ravi";
for a in name:
    print(a)

# COMMAND ----------

# range within for loop
for a in range(5):
    print(a)

# COMMAND ----------

# MAGIC %md
# MAGIC Break and contiune
# MAGIC
# MAGIC Break: With the break stmt we can stop the loop before it has looped throught all the items. it break entire loop.
# MAGIC
# MAGIC Contiune: skip match value and contine 
# MAGIC

# COMMAND ----------

fruits=['apple','Banana','cherry','Orange','mango','Kiwi']
for x in fruits:

  if x == 'cherry':
    break
  print(x)
  print('another state')

# COMMAND ----------

fruits=['apple','Banana','cherry','Orange','mango','Kiwi']
for x in fruits:

  if x == 'cherry':
    continue
  print(x)
  print('another state')

# COMMAND ----------

for i in range (20):
    if i in[1,3,4]:
        continue
    print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC The while loop
# MAGIC
# MAGIC With the while loop we can execute a set of stmt as long as condition is true
# MAGIC
# MAGIC syantax while condition:
# MAGIC
# MAGIC        'statement'

# COMMAND ----------

i=0
while i <10:
  i=i+1
  print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC The break stmt
# MAGIC
# MAGIC With the break stmt we can stop the loop even if the while condition is true

# COMMAND ----------

i=0
while i < 10:
    i +=1
    if i==5:
        break
    print(i)

# COMMAND ----------

