import numpy as np
import pandas as pd

# =========================================================================
# SERIES: Temp Dataset Cleaning - Challenge #2 (Foreign Employee Dataset)
# TARGETS: Fix NaNs in Age/Experience, clean city names, and fix Join_Date
# =========================================================================

dirty_data = {
    "Emp_ID": list(range(501, 531)),
    
    "Emp_Name": ["John", "Emily", "Michael", "Jessica", "David", "Sarah", "James", "Karen", "Robert", "Lisa",
                 "William", "Nancy", "Daniel", "Betty", "Matthew", "Sandra", "Anthony", "Ashley", "Mark", "Dorothy",
                 "Donald", "Kimberly", "Steven", "Emily", "Paul", "Donna", "Andrew", "Michelle", "Joshua", "Carol"],
    
    "Age": [28, 35, np.nan, 42, 22, 31, 55, np.nan, 12, 40,
            33, 48, 26, np.nan, 62, 29, 37, 110, 45, 23,
            np.nan, 34, 50, 16, 27, 41, np.nan, 38, 49, 32],
            
    "City": ["new york", "  NEW YORK  ", "london", "London", "LONDON", "paris", "Paris", "  PARIS", "tokyo", "Tokyo",
             "new york", "London", "paris", "Tokyo", "berlin", "Berlin", "new york", "London", "paris", "Tokyo",
             "BERLIN", "  LONDON", "Paris", "Tokyo", "Berlin", "new york", "London", "paris", "Tokyo", "Berlin"],
             
    "Experience_Years": [5, 12, 8, np.nan, 1, 7, 25, 14, np.nan, 15,
                        9, 20, 3, 11, np.nan, 6, 13, 85, 18, 2,
                        10, np.nan, 22, 0, 4, 16, np.nan, 11, 21, 8],
                        
    "Join_Date": ["2021-05-10", "2014-08-22", "2018-11-05", "2020-03-15", "2025-01-20", "2019-07-11", "2001-12-01", "2012-04-18", "2026-02-10", "2011-09-05",
                 "2017-06-30", "2006-10-12", "2023-02-28", "2015-05-14", "2026-05-01", "2020-09-19", "2013-11-25", "1940-01-01", "2008-04-03", "2024-10-15",
                 "2016-07-22", "2026-01-10", "2004-05-19", "2026-03-01", "2022-12-15", "2010-02-20", "2026-04-15", "2015-08-08", "2005-01-30", "2018-06-12"]
}

df_Dirty = pd.DataFrame(dirty_data)


print("Dataset Loaded (30 Rows)")
print(df_Dirty.head())



print(df_Dirty)


print(df_Dirty.describe())



print(df_Dirty.info())



df_Dirty.loc[df_Dirty['Age']>100,'Age']=np.nan

print(df_Dirty)


df_Dirty.loc[df_Dirty['Age']<18,'Age']=np.nan


print(df_Dirty)


print(df_Dirty.info())



df_Dirty['Age']=df_Dirty['Age'].fillna(df_Dirty['Age'].median())


print(df_Dirty)


df_Dirty['Age']=df_Dirty['Age'].astype(int)


print(df_Dirty)



df_Dirty['City']=df_Dirty['City'].str.strip().str.upper()


print(df_Dirty)


df_Dirty['Experience_Years']=df_Dirty['Experience_Years'].fillna(df_Dirty['Experience_Years'].median())


print(df_Dirty)


df_Dirty['Experience_Years']=df_Dirty['Experience_Years'].astype(int)


print(df_Dirty)

df_Dirty['Join_Date']=pd.to_datetime(df_Dirty['Join_Date'])

print(df_Dirty['Join_Date'].dtype)


df_Dirty=pd.get_dummies(df_Dirty,columns=['City'],dtype=int)


df_Dirty=df_Dirty.drop_duplicates()

print(df_Dirty)

df_Dirty.to_csv('Dataset temp 1 cleaning.csv',index=False)

# i'm busy so this is temp Dataset i clean :)

# i'm so happy :)
# this is bigning :) (To Be Best Ai Engineer :)...)