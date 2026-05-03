import pandas as pd
print(pd.__version__)
print('\n')
df=pd.DataFrame([11,22,33],columns=["col_Name"])
print(df)
print('\n')
print(type(df))
print('\n')
data={
    'Name':   ['sajan','s2036','k2034'],
    'age':    [18,0,13],
    'salary': [95000,200036,340000]
    
}

df=pd.DataFrame(data)
print(df)
print('\n')

print(df.head())# first 5 rows
print(df.head(3))# first 3 rows
print('\n')
print(df.tail(2))# last 2 rows
print('\n')
print(df.shape) # shape of DataFrame
print('\n')
print(df.columns)# to see column names
print('\n')
print(df.rename(columns={'salary': 'monthly_salary'}))# it not save monthly salary change, it change only in this line
print(df.rename(columns={'salary': 'monthly_salary'},inplace=True))# now it change in 
print('\n')
print(df)
print('\n')
df1=df.rename(columns={'salary':'monthly_salary'})
print(df1)# or storing change in another variable can help
print('\n')
print(df.info())# info about dataframe
print('\n')
print(df.describe())# describe dataframe in statistical form for numerical columns
print('\n')
# save and load data form csv
print(df.to_csv('first pd file,ks.py'))# export dataframe
print('\n')
load_df=pd.read_csv('first pd file,ks.py')# import dataframe
print(load_df)
print('\n')
# rows and column select

#selecting column
print(df[['Name']])# it print only one column
print('\n')
print(df[['Name','monthly_salary']])# now it print two column [spacific]
print('\n')

#selecting row, index based (label based)
print(df.loc[df.Name=='sajan'])
print("\n")
print(df.loc[(df.Name=='sajan')&(df.monthly_salary>=10000)])# it print spacific column and condition if salary is greater then 10000
print("\n")
print(df.iloc[0])# [only for rows]
#[iloc is only for rows] it print 0th row or value (sajan is in the 0th row and 100000 salary)
print("\n")
print(df.iloc[0:2])
# print first two rows
print("\n")
print(df.iloc[0:2])#[start:stop:step] (iloc, only for rows)
# it print first three rows
print('\n')
print(df.loc[0:2])# it print column from 0 to 2 (last index is included) [loc, only for column]
print('\n')
print(df)
print('\n')
print(df)
print('\n')
print(df[df['age']>15])# print age greater then 15
print('\n')
df_age_filter=df[df['age']>=15]# storing filter data in variable
print('\n')
print(df_age_filter)# printing filter data variable
print('\n')
print(df[(df['age']>15)&(df['monthly_salary']>=10000)])
# only print age graeter 15 and monthly salary greater 10000 only (0 index row)
print('\n')
print(df.where(df['age']>15))
# it not change the whole dataframe, it fill false values with [nan]
print('\n')
print(df.where(df['age']>15, other='not eligible'))
# it print nan values with not not eligible massage
print('\n')
# rows and columns operation (add, update, delete)
print(df)
print('\n')
# adding new column
df['age_of_years']=['18','0','13']# add new team column
print(df)
print('\n')
df['bonus']=df['monthly_salary']*0.09 # adding new bonus column
print(df)
print('\n')
# adding new rows 
df.loc[len(df)]=['sks',18,150000,'18',20026]
print(df)
print('\n')
print(len(df))
print('\n')

# upadte value [using row index]
df.loc[0,'monthly_salary']=100000# it change/update salary in monthly salary column in index number 0 
print(df)
print('\n')

# updating value [using column name] 
df.loc[df.Name=='sajan', 'monthly_salary']=100000
print("\n")

# delete value, [rows and column values]
print(df.drop(df[df.Name=='sks'].index))#(drop row axis 0) only change in this line 
print("\n")
print(df.drop(1,axis=0))#second method drop column by index
df=df.drop(df[df.Name=='sks'].index)# storing changes in same variable or inplace=True
print("\n")
print(df[df.Name=='sks'])
print("\n")

#df.drop('bonus'),axis=1
print(df.drop('bonus',axis=1))#axis 0 is set by default and axis 0 means row and axis 1 means column (deleting bonus column)
print(df.drop('bonus',axis=1, inplace=True))# it change in dataframe
print("\n")
print(df)
print("\n")

# delete multiple columns
print(df.drop(['age','age_of_years'],axis=1))# only change in this line
print("\n")
print(df)
print("\n")
# sorting 
df.rename(columns={'monthly_salary':'salary'}, inplace=True)
print(df.sort_values('salary'))# sort salary column low to high
print("\n")# ascending order default low to high
print("\n")

print(df.sort_values('salary',ascending=False))# salary column high to low 
print("\n")# descending order high to low
# working with date values
df['DOJ']=['2024-01-01','2024-02-02','2024-03-03']# [year:month:date] standard
print("\n")
print(df)
print("\n")
print(df['DOJ'].dtype)
df['DOJ']=pd.to_datetime(df['DOJ'])
print(df['DOJ'].dtype)# if you want changing first dataframe name and [] square bracket and give value under that
print("\n")
df1=df # same object of dataframe means if do changes in one dataframe it will be reflect on second dataframe too (second version)
print(df1)# copy df value to df1, you have write df1=df.copy() that is real copy  
print("\n")

df1['DOJ2']=['01-01-2024','02-02-2024','03-03-2024']# [date:month:year] not in order
print(df1)
print("\n")
print(df1['DOJ2'].dtype)
print("\n")
df1['DOJ2']=pd.to_datetime(df1['DOJ2'],format='%d-%m-%Y')# it order the unorder date and time like [date:month:year] convert in [year:month:date]
print(df1)
print("\n")
print(df1['DOJ'].dtype)# now DOJ is in right time format
print("\n")
print(df)
print("\n")


df=df.drop('DOJ2',axis=1)# delete DOJ2 column
print(df)
print("\n")

# extract years, week, day
print(df['DOJ'].dt.year)# get years
print("\n")
print(df['DOJ'].dt.month)# get month 
print("\n")
print(df['DOJ'].dt.day)# get day
print("\n")
print(df['DOJ'].dt.day_name())# get info about day
print("\n")
df['month']=df['DOJ'].dt.month  
print(df)
print("\n")
print(df['DOJ']+pd.Timedelta(days=90))# add 90 day
print("\n")
# handling missing values
print(df)
print("\n")
print(df.isnull())
print("\n")
import numpy as np
df.loc[df.Name=='sajan','salary']=np.nan
print(df)
print("\n")
print(df.isnull().sum())# it create a list of all nan values
print("\n")
print(df.fillna(0))# fill salary row with 0
print("\n")
df.loc[df.Name=='sajan','salary']=100000
print("\n")

# aggregation and group by
print(df['month'].value_counts)# to count days in month
print("\n")
print(df[df['month']==1].value_counts())# spacific month (1)
print("\n")
# aggregatiion
print(df.groupby('month') ['salary'].sum())#sum of salaries of each month
print("\n")
print(df.groupby('month') ['salary'].mean())# avarage salary in each month
print("\n")
print(df.groupby('month').agg({'salary':'mean','Name':'count'}))
# it print monthly avarage salary,month and number of employees
print("\n")
# concatenate and marging dataframes
df1=pd.DataFrame({'ID':[1,2,3],'Name':['A','B','C']})
print(df1)
print("\n")
df2=pd.DataFrame({'ID':[1,2,2,4],'Score':[88,96,77,79]})
print(df2)
print("\n")
print(pd.concat([df1,df2],axis=0))# vertical 
print("\n")
print(pd.concat([df1,df2],axis=1))# horizantal 
# df1 dont have enough row to cancat with df2 than nan
print("\n")

# marging
print(pd.merge(df1,df2,how='inner',on='ID'))


