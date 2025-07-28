# Databricks notebook source
import pandas as pd
import numpy as np

# COMMAND ----------

import pandas as pd

# COMMAND ----------

df=pd.read_csv("/Volumes/workspace/default/dataset/weather.csv")
df

# COMMAND ----------

# WAP to giev date where city is mumbai
# method 1
df[df['city']=='mumbai']['date']

# COMMAND ----------

# method 2
df['date'][df['city']=='mumbai']

# COMMAND ----------

# WAP to to print avg temp
avg_temp=df['temperature'].mean()
print(avg_temp)

# COMMAND ----------

# WAP to calcuate avg temp in mumbai
avg_temp_mumbai=df['city']=='mumbai',df['temperature'].mean()
print(avg_temp_mumbai)

# COMMAND ----------

# MAGIC %md
# MAGIC Data Munging or data wrangling:
# MAGIC
# MAGIC The process of cleaning messy data is called data munging or data wrangling.
# MAGIC

# COMMAND ----------

# cheke null data
df.isnull().empty

# COMMAND ----------

# fill that empty space with null value
df.fillna(0)

# COMMAND ----------

# MAGIC %md
# MAGIC Database basic:
# MAGIC
# MAGIC It is object in pandas. it is used to represent data with rows and column (tabular or excel spreadshhet like data)

# COMMAND ----------

# creating data frame
df=pd.read_csv("/Volumes/workspace/default/dataset/weather.csv")
df

# COMMAND ----------

# creating datafrmae with python dict
weather_data={
    'Day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'Temp':[32,35,28,24,32,31],
    'Windspeed':[6,7,2,7,4,2],
    'Event':['Rain','Sunny','Snow','Snow','Rain','Sunny']
}

# converting dict into dataframe
weather_data=pd.DataFrame(weather_data)
weather_data

# COMMAND ----------

# print shape of datafrmae
weather_data.shape

# COMMAND ----------

# print row and col seprate
row,column=weather_data.shape
print(row)
print(column)

# COMMAND ----------

# print top 2 row
weather_data.head(2)

# COMMAND ----------

# print last 2 row
weather_data.tail(2)

# COMMAND ----------

# print the col
weather_data.columns

# COMMAND ----------

# print column with row
weather_data.Day # weather_data['Day']

# COMMAND ----------

# cheke type of col
type(weather_data['Day'])

# COMMAND ----------

# print two col
weather_data[['Day','Temp']]

# COMMAND ----------

# find max temp
weather_data['Temp'].max()

# COMMAND ----------

weather_data['Temp'].min()

# COMMAND ----------

# print analysis of all numeric col
weather_data.describe()

# COMMAND ----------

# conditional stmt
weather_data[weather_data.Temp >=30]

# COMMAND ----------

weather_data[weather_data.Temp ==weather_data.Temp.max()]


# COMMAND ----------

# print day when temp is max
weather_data[['Day','Temp']][weather_data.Temp==weather_data['Temp'].max()]

# COMMAND ----------

weather_data.index

# COMMAND ----------

# changing index
weather_data.set_index('Day')

# COMMAND ----------

weather_data

# COMMAND ----------

weather_data.loc['1/3/2017']

# COMMAND ----------

# reset the index
weather_data.reset_index()

# COMMAND ----------

# MAGIC %md
# MAGIC Different way make dataframe

# COMMAND ----------

# creating dataframe with import csv method using pandas
import pandas as pd
df=pd.read_csv("/Volumes/workspace/default/dataset/weather.csv")
df

# COMMAND ----------

# creating df usinf tuple
import pandas as pd
data=[(
    '1/01/2025',32,6,'Rain'),
      ('1/02/2025',35,7,'Sunny'),
      ('1/03/2025',28,9,'Snow'),
      ('1/04/2025',24,12,'Snow'
)]
df=pd.DataFrame(data,columns=['Day','Temp','Windspeed','Event'])
df



# COMMAND ----------

# uisng list of dict
import pandas as pd
data=[(
    '1/01/2025',32,6,'Rain'),
      ('1/02/2025',35,7,'Sunny'),
      ('1/03/2025',28,9,'Snow'),
      ('1/04/2025',24,12,'Snow'
)]
values=[
    'Day','Temp','Windspeed','Event'
]
df=pd.DataFrame(data,columns=values)
df

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Handling missing values and data

# COMMAND ----------

import pandas as pd
import numpy as np
df=pd.read_csv("/Volumes/workspace/default/dataset/wh.csv",
               parse_dates=["Date"])
df

# COMMAND ----------

# set Date as index
df.reset_index('Date',inplace=True)
df

# COMMAND ----------

# cheking null value 
df.isnull().sum()

# COMMAND ----------

# filling null value with 0
new_df=df.fillna(0)
new_df

# COMMAND ----------

# filling the null value column wise
new_df=df.fillna({
    'Temp':0,
    'Windspeed':0,
    'Event':'No event'
})
new_df


# COMMAND ----------

# filling 0 with pre value
new_df=df.fillna(method='ffill')
new_df

# filling value with next value
new_df=df.fillna(method='bfill')
new_df

# COMMAND ----------

new_df.isnull().sum()

# COMMAND ----------

# filling null value with mean
new_df=df.fillna(df.mean())
new_df

# COMMAND ----------

# filling Event null value with mode
new_df=df.fillna(df.mode().iloc[0])
new_df

# COMMAND ----------

# MAGIC %md
# MAGIC Dropna: 
# MAGIC
# MAGIC Dropna is used to drop the vlaue

# COMMAND ----------

# droping null value
new_df=df.dropna()
new_df

# COMMAND ----------

# MAGIC %md
# MAGIC 17/04/2025
# MAGIC
# MAGIC Handling missing Data: fillna , dropna

# COMMAND ----------

import numpy as pd
import numpy as np

# COMMAND ----------

import pandas as pd
df=pd.read_csv("/Volumes/workspace/default/dataset/wh.csv")
df

# COMMAND ----------

# checking data type of each column
df.dtypes

# COMMAND ----------

# MAGIC %md
# MAGIC in this dataset date dtypes is object. so we convert date inte dtypes.

# COMMAND ----------

# converting date into date types
df['Date']=pd.to_datetime(df['Date'])

# now cheke types of Date 
df.dtypes

# COMMAND ----------

# set date as index
df.set_index('Date',inplace=True)

# COMMAND ----------

df

# COMMAND ----------

# checke null values
df.isnull().sum()

# COMMAND ----------

# fill that null value with 0
new_df=df.fillna(0)

# COMMAND ----------

# filling null value with dict
new_df=df.fillna({
        'Temp':0,
        'Windspped':0,
        'Event':'No Event'
})

new_df
            

# COMMAND ----------

# filling temp, windspeed, Event by previous value
new_df=df.fillna(method='ffill') # ffill= fowward fill
new_df

# COMMAND ----------

# still in windspeed we got 2 null value so we can fill that value with backfill method
new_df['Windspped'] = new_df['Windspped'].fillna(method='bfill') 
new_df

# COMMAND ----------

# sppose we want fill forward and backword only one time than we used limit function
new_df=df.fillna(method='ffill',limit=1)

# COMMAND ----------

# interplolation method is linear method
new_df=new_df.interpolate()
new_df

# COMMAND ----------

# interpolation method using time
new_df=new_df.interpolate(method="time")
new_df

# COMMAND ----------

new_df=df.interpolate(method="time")
new_df

# COMMAND ----------

# dropping nan value
new_df=df.dropna()
new_df

# COMMAND ----------

# condition drop i want drop value where all column of value null
new_df=df.dropna(how='all')
new_df

# COMMAND ----------

# thresh used to drop value where threshhold is less than 2 or any condition
new_df=df.dropna(thresh=2)

# COMMAND ----------

# filling date  null value 
df=pd.date_range("01-01-2017","01-11-2017")
idx=pd.DatetimeIndex(df)
df.reindex(idx,inplace=True)

# COMMAND ----------

# MAGIC %md
# MAGIC Handling Missing data: replace function
# MAGIC
# MAGIC Syantax: df.replace(past_value,new_value)

# COMMAND ----------

import pandas as pd
df=pd.read_csv("/Volumes/workspace/default/dataset/wh_replace.csv")
df

# COMMAND ----------

import numpy as np
New_df=df.replace(-9999.99,np.nan)
New_df

# COMMAND ----------

# replace multiple value using list
New_df=df.replace([-9999.99,-9999],np.nan)

# COMMAND ----------

New_df

# COMMAND ----------

import pandas as pd
df1=pd.read_csv("/Volumes/workspace/default/dataset/wh_r1eplace.csv")
df1

# COMMAND ----------

# replace multiple column value with 0 using dict 
import numpy as np
new_df=df1.replace(
    {
        'Temp':-9999.99,
        'Winspeed':-9999.99,
        'Event':'0'

    },np.nan)

new_df

# COMMAND ----------

df1
# Replace -99999.99  with np.nan and 0 with 'Sunny'
new_df=df1.replace(
    {
        -9999.99:np.nan,
        0:'sunny'
    }
)
new_df

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Group by: Split Apply Combine

# COMMAND ----------

import pandas as pd
import numpy as np
df2=pd.read_csv("/Volumes/workspace/default/dataset/wh_groupby.csv")
df2

# COMMAND ----------


groupby_city=df2.groupby('City')
groupby_city
for city,city_df in groupby_city:
    print(city)
    print(city_df)

# COMMAND ----------

# group by specific city
groupby_city=df2.groupby('City')
groupby_city.get_group('New York')

# COMMAND ----------

groupby_city.max()

# COMMAND ----------



# COMMAND ----------

# avg
groupby_city.mean()

# COMMAND ----------

groupby_city.describe()

# COMMAND ----------

import matplotlib.pyplot as plt
groupby_city.plot()

# COMMAND ----------

# MAGIC %md
# MAGIC Concating 2 dataframe

# COMMAND ----------

import pandas as pd
Indaia_wh={
    'City':['pune','mumbai','delhi'],
    'Temp':[32,45,30],
    'Windspeed':[3,12,40]
}
india_df=pd.DataFrame(Indaia_wh)
india_df


# COMMAND ----------

usa_whether={
    'City':['new york','chicago','orlando'],
    'Temp':[21,14,35],
    'Windspeed':[12,16,2]
}
city_df=pd.DataFrame(usa_whether)
city_df


# COMMAND ----------

# concating two df
pd.concat([india_df,city_df])

# COMMAND ----------

# concat df with contiune index
df=pd.concat([india_df,city_df],ignore_index=True)


# COMMAND ----------

df=pd.concat([india_df,city_df],keys=['indai','us'])

# COMMAND ----------

import pandas as pd
temp_df=pd.DataFrame(
    {
        "City":['A','B','C'],
        "Temp":[14,23,34]
    },index=[0,1,2]
)
wind_df=pd.DataFrame(
    {
        'City':['A','B','C'],
        'Windspeed':[12,16,2]
    },index=[0,1,2])


# COMMAND ----------

df=pd.concat([temp_df,wind_df],axis=1)
df

# COMMAND ----------

temp_df

# COMMAND ----------

s=pd.Series(['Humid','Dry','Rainy'],name='Event')
df=pd.concat([temp_df,s],axis=1)
df

# COMMAND ----------

# MAGIC %md
# MAGIC Merge

# COMMAND ----------

df=pd.DataFrame({
    'Roll_no':[1,2,3,4],
    'Std_name':['A','B','C','D']
},index=[1,2,3,4])

df1=pd.DataFrame({
    'Roll_no':[1,2,3,4,5],
    'Mark':[12,14,15,18,20]
    },index=[1,2,3,4,5])


# COMMAND ----------

df2=pd.merge(df,df1,on="Roll_no") # by default it perform inner join
df2

# COMMAND ----------

df2=pd.merge(df,df1,on='Roll_no',how='left') # left join
df2

# COMMAND ----------

df2=pd.merge(df,df1,on='Roll_no',how='right',indicator=True) # left join
df2

# COMMAND ----------

# MAGIC %md
# MAGIC pivot and pivot table

# COMMAND ----------

df=pd.DataFrame({
  'Name':['A','B','C'],
  'City':['Delhi','Mumbai','Delhi'],
  'Temp':[1,2,3],
  'Humidity':[1,2,3]
})
df

# COMMAND ----------

df.pivot(index='City',columns='Temp')

# COMMAND ----------

import pandas as pd

# Create the DataFrame
data = {
    'date': ['5/1/2017', '5/1/2017', '5/2/2017', '5/2/2017',
             '5/1/2017', '5/1/2017', '5/2/2017', '5/2/2017'],
    'city': ['new york', 'new york', 'new york', 'new york',
             'mumbai', 'mumbai', 'mumbai', 'mumbai'],
    'temperature': [65, 61, 70, 72, 75, 78, 62, 80],
    'humidity': [56, 54, 60, 62, 80, 83, 85, 26]
}

df = pd.DataFrame(data)

print(df)


# COMMAND ----------

df.pivot_table(index='city',columns='date')


# COMMAND ----------

# agg 
df.pivot_table(index='city',columns='date',aggfunc='sum')

# COMMAND ----------

df.pivot_table(index='city',columns='date',margins=True)

# COMMAND ----------

df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.pivot_table(index=pd.Grouper(freq='M'), columns='city')

# COMMAND ----------



# COMMAND ----------

