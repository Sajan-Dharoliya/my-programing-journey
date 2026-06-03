import numpy as np
import pandas as pd


dirty_data = {
    "Emp_ID": list(range(601, 631)),
    
    "Emp_Name": ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth",
                 "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen",
                 "Christopher", "Nancy", "Daniel", "Lisa", "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra"],
    
    "Age": [29, 41, np.nan, 33, 52, 135, 26, 38, np.nan, 22, 
            47, 31, 28, np.nan, 61, 24, 35, 12, 44, np.nan, 
            30, 55, 27, np.nan, 40, 34, 49, np.nan, 23, 36],
            
    "City": ["new york", "  NEW YORK  ", "london", "London", "LONDON", "paris", "Paris", "  PARIS", "tokyo", "Tokyo",
             "new york", "London", "paris", "Tokyo", "berlin", "Berlin", "new york", "London", "paris", "Tokyo",
             "BERLIN", "  LONDON", "Paris", "Tokyo", "Berlin", "new york", "London", "paris", "Tokyo", "Berlin"],
             
    "Salary_USD": ["$52000", "$89000", "$41000", np.nan, "$63000", "$95000", "$48000", "$72000", np.nan, "$39000",
                    "$115000", "$58000", "$51000", "$67000", np.nan, "$43000", "$76000", "$15000", "$82000", np.nan,
                    "$105000", "$91000", "$46000", "$74000", "$88000", np.nan, "$55000", "$98000", "$42000", "$69000"]
}

df_dirty = pd.DataFrame(dirty_data)


print("Dataset Loaded (30 Rows)")
print(df_dirty.head())






print(df_dirty)


print(df_dirty.info())




df_dirty.loc[df_dirty['Age']>100,'Age']=np.nan

df_dirty.loc[df_dirty['Age']<18,'Age']=np.nan

print(df_dirty)



df_dirty['Age']=df_dirty['Age'].fillna(df_dirty['Age'].median())


print(df_dirty)



df_dirty['Age']=df_dirty['Age'].astype(int)


print(df_dirty['Age'].dtype)


print(df_dirty)



df_dirty['City']=df_dirty['City'].str.strip().str.upper()

print(df_dirty)

df_dirty['Salary_USD']=df_dirty['Salary_USD'].str.replace('$','',regex=False)


print(df_dirty)

df_dirty['Salary_USD']=df_dirty['Salary_USD'].astype(float)


df_dirty.loc[df_dirty['Salary_USD']>100000,'Salary_USD']=np.nan


df_dirty['Salary_USD']=df_dirty['Salary_USD'].fillna(df_dirty['Salary_USD'].median())



print(df_dirty)



df_dirty['Salary_USD']=df_dirty['Salary_USD'].astype(int)



print(df_dirty)

print(df_dirty['Salary_USD'].dtype)


print(df_dirty)




df_dirty=pd.get_dummies(df_dirty,columns=['City'],dtype=int)

print(df_dirty)



df_dirty=df_dirty.drop_duplicates()


print(df_dirty)




df_dirty.to_csv('Dataset temp 3 cleaning.csv',index=False)



# i'm busy so this is temp Dateset i clean :)

# i'm so happy :)
# this is bigning :) (To Be Best Ai Engineer :)...)