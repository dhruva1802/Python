# Databricks notebook source
Data={
    'Day':['Mon','Tue','Wed','Tur','Fri','Sat','Sun'],
    'Temp':[20,21,22,23,24,25,26],
    'Windspeed':[10,11,12,13,14,15,16]
}

import pandas as pd
df=pd.DataFrame(Data)

# COMMAND ----------

df1=pd.melt(df,id_vars=['Day'])
df1

# COMMAND ----------

# converting df1 into original df
original_df=df1.pivot(index='Day',columns='variable',values='value').reset_index()
original_df

# COMMAND ----------

# MAGIC %md
# MAGIC Stack and unstack

# COMMAND ----------

stack_df=df.stack()


# COMMAND ----------

# stack to unstack
stack_df.unstack()

# COMMAND ----------

# MAGIC %md
# MAGIC Read and Write Data from Database(SQL)

# COMMAND ----------

import pandas as pd
import numpy as np

# COMMAND ----------

# Load the data using spark
df = spark.sql("SELECT * FROM samples.bakehouse.media_customer_reviews")

# to convert to Pandas
df=df.toPandas()
df.head(5)



# COMMAND ----------

# Reading data from CSV file using sql
df1 = spark.read.csv("/Volumes/workspace/default/dataset/weather.csv", 
                     header=True, 
                     inferSchema=True)

# Create a temporary view
df1.createOrReplaceTempView("weather_data")

# Now you can write SQL queries on this data
result = spark.sql("SELECT * FROM weather_data WHERE temperature =65")

# Display the result
display(result)

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC