# Databricks notebook source
# MAGIC %md
# MAGIC Function
# MAGIC
# MAGIC The keyword def introduces a function defination.
# MAGIC
# MAGIC It must be followed by the function name and parenthesized list of formal parameters.
# MAGIC
# MAGIC The stmt that form the body of the funtion start at the next line and must be indented.
# MAGIC
# MAGIC A function is a black of code which only run when it is called.
# MAGIC
# MAGIC you can pass data, knows as parameters into a function
# MAGIC
# MAGIC A function can return data as a result

# COMMAND ----------

# lambda function
# single line
lambda_fun=lambda a: a+10   # a is argu and a+10 is exp
lambda_fun(10)
type(lambda_fun)

# COMMAND ----------

# double line
lambda_fun=lambda a,b:a+b
lambda_fun(10,20)

# COMMAND ----------

# multiple exp
lambda_fun=lambda a,b:(a+b,a*b,a-b)
lambda_fun(10,20)

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC in other langu funtion and procedures and seprate
# MAGIC
# MAGIC but in python function and procedure are same
# MAGIC
# MAGIC function : fucntion + procedure (in python)
# MAGIC
# MAGIC function used for calcuation purpose and returning some value agg
# MAGIC
# MAGIC procedure : step by step process
# MAGIC
# MAGIC Def func_name (arg)

# COMMAND ----------

# method 1
def fun_name(a,b):
  return a+b
fun_name(10,20)

# COMMAND ----------

# method 2
def fun_name(a,b):
  print('sum of a and b are:',a+b)
fun_name(1,2)

# COMMAND ----------

# MAGIC %md
# MAGIC  Creating function

# COMMAND ----------

# creating function
def my_fun():
  print("hellow from a function")
  print("stmt two")
  print("stmt three")

# calling or executing function
my_fun()

# COMMAND ----------

# Creating function with two argument a and b
def my_sum(a,b):
    print("Sum of a and b value is:",a+b)

# calling the fun
result=my_sum(10,20)
print("result is:",result)

# COMMAND ----------

# create fun for create cul
def cul(a,b):
    print("Sum of a and b value is:",a+b)
    print("sub of a and b value is:",a-b)
    print("Mul of a and b value is:",a*b)
    print("Div of a and b value is:",a/b)


cul(10,20)
cul(20,20)


# COMMAND ----------

# MAGIC %md
# MAGIC Agruments (parameters)
# MAGIC Information can be passed into function as arguments.
# MAGIC
# MAGIC function argument: positional keyword
# MAGIC
# MAGIC A function is most useful when argument are passed to the function
# MAGIC New value for times are procedded inside the function
# MAGIC position argument are processed in other they are createed in.

# COMMAND ----------

# postiopn based based
def my_fun(fname,age):
  print("my name is:",fname)
  print("my age is:",age)
# calling the fun
my_fun("ravi",35) # position bsed

# COMMAND ----------

# keyword based
my_fun(fname='ravi',age=35)

# COMMAND ----------

# create fun for stu info
def student(name,age,rollno,per):
    print("student name is:",name)
    print("student age is:",age)
    print("student rollno  is:",rollno)
    print("student per is:",per)
# postion based 
student("ravi",35,21,75)

# keyword based
student(name="ravi",age=35,rollno=21,per=75)

# COMMAND ----------



# COMMAND ----------

# fun with specific datatype
def student(name:str,age:int,rollno:int,per:float):
    print("student name is:",name)
    print("student age is:",age)
    print("student rollno  is:",rollno)
    print("student per is:",per)
# postion based 
student("ravi",35,21,75.0)

# keyword based
student(name="ravi",age=35,rollno=21,per=75.0)

# COMMAND ----------

# MAGIC %md
# MAGIC keyword argu are processed by key, value and have default values.
# MAGIC
# MAGIC You can also send argument with the key= value syntax
# MAGIC
# MAGIC one handly features of keyword argument is that you can set default and only changes the defalut you want to changes

# COMMAND ----------

def my_fun(age=55,fname="ravi"):
  print("my name is:",fname)
  print("my age is:",age)
my_fun(age=55,fname='ravi')

# COMMAND ----------

def my_fun(name,age,loc="india"): # loc is defalut argu
    print("my name is:",name)
    print("my age is:",age)
    print("i am from:",loc)
my_fun("ravi",24)
print() # for space bet 2 result
my_fun("ravi",24,"uk")


# COMMAND ----------

# create fun two create even list
def check_even_list(num_list):
    even=[]
    for number in num_list:
        if number%2==0:
            even.append(number)
        else:
            pass
    return even

check_even_list([1,2,3,4,5,6,7,8,10])


# COMMAND ----------

# WAP fun to check odd or not
def odd_list(num_list):
    odd = []
    for number in num_list:
        if number % 2 == 1:
            odd.append(number)
    return odd

odd_list([1,2,3,4,5,6,7])

# COMMAND ----------

# MAGIC %md
# MAGIC Variable Number of argument (*args)
# MAGIC
# MAGIC In cases where you don't know the exact number of argument that you want to pass to as function.
# MAGIC
# MAGIC You can use the following syantax with *args

# COMMAND ----------

# creating the fun
def my_sum(*args): # args with value
  return sum(args)

# calling the fun
my_sum(10,20)

# COMMAND ----------

def my_std(**kvargs): # key and value function
    print("key value pair data:",kvargs)

my_std(name="ravi",age=35,roll_no=21)

# COMMAND ----------

# MAGIC %md
# MAGIC The pass Statment
# MAGIC
# MAGIC Function defination cannot be empty, but if ypu for some reson have a function with no content.
# MAGIC
# MAGIC put in the pass stmt to avoid getting an error

# COMMAND ----------

def func():
  pass