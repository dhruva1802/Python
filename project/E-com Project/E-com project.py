# Databricks notebook source
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# COMMAND ----------

Cust_data=pd.read_csv("/Volumes/workspace/default/raw_data/customer_table.csv")
order_data=pd.read_csv("/Volumes/workspace/default/raw_data/order_table.csv")
Product_data=pd.read_csv("/Volumes/workspace/default/raw_data/product_table.csv")

# COMMAND ----------

Cust_data.head(5)


# COMMAND ----------

order_data.head(5)


# COMMAND ----------

Product_data.head(5)

# COMMAND ----------

Cust_data.columns

# COMMAND ----------

order_data.columns


# COMMAND ----------

Product_data.columns


# COMMAND ----------

Cust_data.dtypes

# COMMAND ----------

# Convert Pandas to PySpark DataFrame
cust_df = spark.createDataFrame(Cust_data)
order_df = spark.createDataFrame(order_data)
product_df = spark.createDataFrame(Product_data)


# COMMAND ----------

Cust_data_spark = spark.createDataFrame(Cust_data)
order_data_spark = spark.createDataFrame(order_data)
Product_data_spark = spark.createDataFrame(Product_data)

Cust_data_spark.write.mode("overwrite").saveAsTable("workspace.default.transform_data_cust")

order_data_spark.write.mode("overwrite").saveAsTable("workspace.default.transform_data_order")

Product_data_spark.write.mode("overwrite").saveAsTable("workspace.default.transform_data_product")

# COMMAND ----------

