# Databricks notebook source
import pandas as pd
import numpy as np

# COMMAND ----------

df=pd.read_csv("/Volumes/workspace/default/dataset/aapl.csv")
df.head(5)

# COMMAND ----------

# MAGIC %md
# MAGIC handling time series data

# COMMAND ----------

df.dtypes

# COMMAND ----------

# MAGIC %md
# MAGIC here Date type is object, we need to convert it into data_stamp and also set index

# COMMAND ----------

new_df=pd.read_csv("/Volumes/workspace/default/dataset/aapl.csv",parse_dates=['Date'],index_col='Date')
new_df.head(5)


# COMMAND ----------

# slicing data using date
new_df.loc['2017-01-01':'2017-01-05']

# COMMAND ----------

# find avg price of apples stock in jan 2017
new_df.loc['2017-01-01' :'2027-01-30'].Close.mean()

# COMMAND ----------

# find avg price of apples volumn in jan 2017
new_df.loc['2017-01-01':'2017-01-30','Volume'].mean()


# COMMAND ----------

# price on 2017-01-03
new_df.loc["2017-01-03"]

# COMMAND ----------

# monthly data
new_df.resample('M').mean()

# COMMAND ----------

# daily data
new_df.resample('D').mean()
# weekly data
new_df.resample('W').mean()
# yearly data
new_df.resample('Y').mean()

# COMMAND ----------

# plot montly plot
new_df.resample('M').mean().Close.plot()


# COMMAND ----------

# Q plt
new_df.resample('Q').mean().Close.plot()


# COMMAND ----------

# Q plt
new_df.resample('Q').mean().Close.plot(kind='bar')

# COMMAND ----------

# Q plt
new_df.resample('Q').mean().Close.plot(kind='box')

# COMMAND ----------

new_df.Close.plot()

# COMMAND ----------

# MAGIC %md
# MAGIC Date_range

# COMMAND ----------

# drop date 
df2 = df.drop(columns=['Date'])
df2.head(2)

# COMMAND ----------

# create date for df2
rng = pd.date_range(start='6/1/2017', end='6/30/2017', freq='B')
rng

# COMMAND ----------

rnd=pd.date_range(start='6/1/2017', end='6/30/2017', freq='B')
rnd

# COMMAND ----------

import numpy as np
ts=pd.Series(np.random.randint(1,10,len(rnd)),index=rnd)
ts.head(5)

# COMMAND ----------

# MAGIC %md
# MAGIC shifting and lagging time in pandas

# COMMAND ----------

import pandas as pd
data={
  'Date':['2017-06-01','2017-06-02','2017-06-03','2017-06-04','2017-06-05','2017-06-06','2017-06-07','2017-06-08','2017-06-09','2017-06-10','2017-06-1'],
  'Open':[10,11,12,13,14,15,16,17,18,19,20]
}
df=pd.DataFrame(data)
df.plot(kind='bar')
df1=df.shift(1)
df1.plot(kind='bar')

# COMMAND ----------

