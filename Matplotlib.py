# Databricks notebook source
# MAGIC %md
# MAGIC It is open sources plotting library developed by John Hunter. create plots, figures, and visualizations using the Python programming language and the NumPy, Pandas, and Matplotlib libraries.

# COMMAND ----------

# MAGIC %md
# MAGIC Line Graph:
# MAGIC
# MAGIC Used to compaire to variable, display on x and y axis. it comparises two axes called 'X-axis' and the 'y-axis'. The horizontal axis is called the x-axis whereas vertical is called y-axis. 

# COMMAND ----------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# COMMAND ----------

Month=np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
rainfall=np.array([100,120,150,180,200,220,25,200,180,150,120,100])
plt.plot(Month,rainfall)
plt.xlabel('Month')
plt.ylabel('Rainfall')
plt.title('Rainfall in a year')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Hist Plot: 
# MAGIC
# MAGIC A hist plot used to rep to show freq distrubtions.

# COMMAND ----------

# hist plot always take input as 1 parameter
Mark=np.array([10,25,46,56,70])
plt.hist(Mark,bins=5)
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.title('Histogram of Marks')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Scatter:
# MAGIC
# MAGIC A Scatter plot is chart that display the relationship bet two variable. A dot rep each value in dataa set

# COMMAND ----------

import numpy as np
import matplotlib.pyplot as plt

Mark_group1 = np.array([10, 25, 46])
Mark_group2 = np.array([56, 70, 50])
mark_dist = np.array([10, 20, 30])

plt.scatter(Mark_group1, mark_dist, color='red')
plt.scatter(Mark_group2, mark_dist, color='blue')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.title('Histogram of Marks')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Line plot:

# COMMAND ----------

dataframe=pd.DataFrame({
  'Cricket_Bat':['SG','MRP','GM','SR'],
  'Price':[1000,2000,1500,4000],
  'Quantity':[10,20,15,40]
})
plt.plot(dataframe['Cricket_Bat'],dataframe['Price'])
plt.xlabel('Cricket_Bat')
plt.ylabel('Price')
plt.title('Cricket_Bat')
plt.grid() # used to plot grid
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Pie plot

# COMMAND ----------

plt.pie(dataframe['Quantity'],labels=dataframe['Cricket_Bat'])
plt.show()
plt.bar(dataframe['Cricket_Bat'],dataframe['Quantity'])
plt.show()
plt.boxplot(dataframe['Price'])
plt.show()
plt.scatter(dataframe['Cricket_Bat'],dataframe['Price'])
plt.show()

# COMMAND ----------

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))
plt.pie(
    dataframe['Quantity'],
    labels=dataframe['Cricket_Bat'],
    autopct='%1.1f%%',  # This shows percentages with 1 decimal place
    startangle=140      # Optional: rotates the start angle for better look
)
plt.title("Distribution of Quantity by Cricket Bat")
plt.axis('equal')  # Equal aspect ratio ensures the pie is a circle.
plt.show()
