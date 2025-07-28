# Databricks notebook source
# MAGIC %md
# MAGIC Varibles: a variable acts as a named container or placeholder in computer memory used to store data values.
# MAGIC python is case censitive lang

# COMMAND ----------

# both name and Name are different
name="Dhruv Daware";
Name="Dhruv Daware";
print("name",name);
print("Name",Name);
print(id(name));
print(id(Name))

# COMMAND ----------

age=30;
print("age is",age);
print(type(age));
help(age);
print(id(age))

# COMMAND ----------

list=[1,2,3,4];
print(list);
print(list[1])

# COMMAND ----------

# MAGIC %md
# MAGIC What is python Identifier?
# MAGIC
# MAGIC . Python identifier is the name we given to identify a variable, list, sets,dict,class, module or object. That means whenever we want to give an entity a name that's called identifier.
# MAGIC
# MAGIC . Sometimes variable and identifier are often misunderstand as same but they are not same

# COMMAND ----------

name="Ravi";
name="ram";
print(name);
print(name[1])

# COMMAND ----------

# memory allcation for int 
a=100;
b=5;
print('a variable id is:',id(a));
print('b variable id is',id(b));

# COMMAND ----------

# local variable we create with v_name
# global variable we can create with gv_name
# global variable can be used in local variable
# local variable can not be used in global variable

# COMMAND ----------

n_name="Dhruv";
gv_name="Daware";
print(n_name,gv_name);

# COMMAND ----------

num1 =55;
num2=11
print(num1+num2)

# COMMAND ----------

Age=35;
Name='Dhruv';
print('My age=%d,My name is %s'%(Age,Name))


# COMMAND ----------

# typecast
Num1=30;
Num2='35';
print(Num1+int(Num2));

# COMMAND ----------

# typecast
num1=35
print(str(num1))
print(type(str(num1)))

# COMMAND ----------

num1='35';
num2=40;
num3=int(num1)+num2;
print(num3);
print(type(num3))

# COMMAND ----------

# Creating Variable and assigning a values
a=b=c=d=55;
a='sample'
print('a value is:',a)
print('b value is:',b)
print('c value is:',c)
print('d value is:',d)

# COMMAND ----------

a=6;
b=2;
c=a/b; # div operator always give answer in float
d=a//b; # if we want answer wihtout float vaue than we used //
print('c value is:',c)
print('d value is:',d)

# COMMAND ----------

# if want reamindor than we used % operator
a=6;
b=2;
print(a%b);

# COMMAND ----------

# f string: 
c_count=40;
target_count=30;
reject=10;
print(f'source count is:{c_count} tearget_count is:{target_count} reject count is:{reject}')

# COMMAND ----------

# format() function
# method 1
name='Dhruv'
age=24
address="nashik"
print('My name is {} and age is {} and address is {}'.format(name,age,address))

# COMMAND ----------

# method 2
name='Dhruv'
age=24
address="nashik"
print('My name is {0} and age is {1} and address is {2}'.format(name,age,address))

# COMMAND ----------

# format specifier
# strings=%s
# integer=%d
# float=%f
# boolean=%b
# complex=%c
# octal=%o
# hexadecimal=%x
# scientific=%e
# percentage=%%

# COMMAND ----------

Age=30;
Name='Dhruv'
print("My name is %s and my age %d"%(Name,Age))

# COMMAND ----------

age=30;
Name='Ram';
Roll_no=21;
print("My age is %d and my name is %s and roll_no is %d"%(age,Name,Roll_no))


# COMMAND ----------

# field convsation
age=30;
Name='Ram';
Roll_no=21;
print("My age is %f and my name is %s and roll_no is %d"%(age,Name,Roll_no))

# COMMAND ----------

# indes in python
name="Dhruv"
name[0]
name[-1]s