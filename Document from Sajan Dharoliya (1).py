import pandas as pd
print(pd.__version__)
print("\n")

df=pd.DataFrame([11,22,33],columns=['col_Name'])
print(df)
print("\n")
print(type(df))
print("\n")

data={
    'Name':['Madhav','Vishakha','Lalita','Rishab'],
    'Age': [16,17,18,19],
    'salary':[90000,70000,50000,30000]
}

print(type(data))
print("\n")

df=pd.DataFrame(data)
print(df)
print("\n")

print(type(df))
print("\n")

print(df.head())#top 5 rows
print("\n")
print(df.tail())#last 5 row
print("\n")

print(df.shape)# shape of dataframe (4,3)
print("\n")

print(df.columns)# column names
print("\n")


print(df.rename(columns={'salary':'Monthly_Salary'}))# not change in dataframe
print("\n")

print(df.rename(columns={'salary':'Monthly_Salary'},inplace=True))# change in dataframe
print("\n")

print(df)
print("\n")

print(df.info())# dataframe info(how much null values, numeric values, columns count)
print("\n")

print(df.describe())# statistical summary of numerical columns in dataframe
print("\n")

# save and load csv file

print(df.to_csv('csv_two.csv'))# export dataframe
print("\n")

load_df=pd.read_csv('csv_two.csv')# import dataframe
print(load_df)

#column selection

print(df[['Name']])# single column
print("\n")

print(df[['Name', 'Monthly_Salary']])# multiple column
print("\n")

#loc - index name based
print(df.loc[df.Name=='Madhav'])# Name column's madhav row's values, wll be print/selected
print("\n")
print(df.loc[(df.Name=='Madhav')&(df.Monthly_Salary>=50000)])# if both condition is true this print other wise don't
print("\n")
print(df.loc[df.Age==17])# Age column wise
print("\n")
print(df.loc[0:2])# include last value

#iloc - index value based

print(df.iloc[0])# it print 0th index row and there columns
print("\n")

print(df.iloc[0:2])# multiple rows 
print("\n")

#filter dataframe
print(df)
print("\n")

print(df[df['Age']>=18])# greater or equal 18 age values will be print [filter]

print("\n")


df_age_filter=df[df['Age']>=18]# storing changes

print(df_age_filter)
print("\n")

print(df[(df['Age']==18)&(df['Monthly_Salary']>=50000)])# filter two conditions
print("\n")


df.where(df['Age']>=18)# print whole dataframe with nan values 
print("\n")


#[update:add:delete] columns and rows

print(df)
print("\n")

# adding new column
df['TEAM']=['CEO','HR','CTO','DA']

print(df)
print("\n")

df['Bonus']=df['Monthly_Salary']*0.2 # adding new Bonus column
print(df)

print("\n")

# adding new row
df.loc[len(df)]=['ABC',21,21000,'IT', 2000]
print(df)
print("\n")

print(len(df))# show rows data
print("\n")


# update values - using index name
df.loc[0,'Monthly_Salary']=95000 # updating Monthly_salary row's 0 index value
print(df)
print("\n")

# using column value
df.loc[df.Name=='Madhav','Monthly_Salary']=90000# updating using madhav row's column monthly_salary
print(df)
print("\n")


# now delete values - rows,columns

print(df.drop(df[df.Name=='ABC'].index))# deleting ABC row, not change in dataframe,
print("\n")
print(df.drop(df[df.Name=='ABC'].index,inplace=True))# change in datframe
print("\n")
print(df)
print("\n")


print(df.drop(1,axis=0))# it delete index number 1 row (index wise)
print("\n")

# deleting column
print(df.drop('Bonus',axis=1,inplace=True))# deleting Bonus column, change in dataframe
print("\n")
print(df)
print("\n")


#sort values
df.rename(columns={'Monthly_Salary':'Salary'},inplace=True)

print(df.sort_values('Salary'))# acsending order (low to high)
print("\n")

print(df.sort_values('Salary',ascending=False))# descending order (high to low)
print("\n")


# working with date values 

df['DOJ']=['2024-01-01','2024-02-15','2024-03-28','2024-03-03']# in order [year:month:date]
print(df)
print("\n")

print(df['DOJ'].dtype)
print("\n")

df['DOJ']=pd.to_datetime(df['DOJ'])# converting DOJ column in datetime formate and storing it

print(df['DOJ'].dtype)
print("\n")

df1=df

df1['DOJ2']=['01-01-2024','15-01-2024','28-03-2024','03-03-2024']
print(df)
print("\n")

print(df1['DOJ2'].dtype)
print("\n")

df1['DOJ2']=pd.to_datetime(df1['DOJ2'],format='%d-%m-%Y')# converting unorder time and date in right order
print(df1)
print("\n")

print(df1['DOJ2'].dtype)
print("\n")

df=df.drop('DOJ2', axis=1)
print(df)
print("\n")

#extracting years,months,week,day

print(df['DOJ'].dt.year)# extracting year
print("\n")


print(df['DOJ'].dt.month)# extracting month
print("\n")


print(df['DOJ'].dt.day)# extracting day
print("\n")


print(df['DOJ'].dt.day_name())# extracting week 
print("\n")

df['Months']=df['DOJ'].dt.month# adding new column
print(df)
print("\n")

df['DOJ']+pd.Timedelta(days=90)# adding 90 days
print(df)
print("\n")

#handling missing values
print(df)
print("\n")

print(df.isnull())
print("\n")

import numpy as np
df.loc[df.Name=='Rishab','Salary']=np.nan# loc use square brackets
print(df)
print("\n")

print(df.isnull())# print all dataframe
print("\n")

print(df.isnull().sum())# it create list of all null values, prasent in dataframe
print("\n")

print(df.fillna(0))# fill null value with 0
print("\n")

df.loc[df.Name=="Rishab",'Salary']=30000 # back to normal dataframe
print("\n")

# aggregation and group by
print(df['TEAM'].value_counts())# team value counts (total values in TEAM column)
print("\n")

print(df[df['Months']==1].value_counts())# it print only whose data who join in janaury
print("\n")

# group by
print(df.groupby('Months')['Salary'].sum())# based on date of joining (Salary aggregation)
print("\n")


print(df.groupby('Months')['Salary'].mean())# avarage salary in each months acording months (based on group by)
print("\n")

# multiple aggregation 
print(df.groupby('Months').agg({'Salary':'mean','Name':'count'}))# multiple aggregation (avarage Salary,Name counts)
print("\n")

# concatenate and marge datafarme
df1=pd.DataFrame({'ID':[1,2,3],'Name':['A','B','C']})
print(df1)
print("\n")

df2=pd.DataFrame({'ID':[1,2,3,4],'Score':[88,96,77,79]})
print(df2)
print("\n")


print(pd.merge(df1,df2,how='outer',on='ID'))
print("\n")

print(pd.merge(df1,df2,how='inner',on='ID'))
print("\n")

print("it's day 7, but i maintand consitency when i'm busy, this is for today :) ")

import numpy as np

# arr=np.array([1,2,3,4,5])
# print(arr)
# print("\n")

# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])
# print(arr[4])
# print("\n")
