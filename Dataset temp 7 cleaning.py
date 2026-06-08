import numpy as np
import pandas as pd

# Generating 100 rows of dirty data
np.random.seed(10)
emp_ids = list(range(1001, 1101))

names_pool = ["Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander",
              "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Sebastian", "Mateo"]
emp_names = [names_pool[i % len(names_pool)] for i in range(100)]

age_pool = [31, np.nan, 24, 45, 50, 19, np.nan, 33, 28, 41, 62, 29, 37, 112, 45, 23, np.nan, 34, 52, 12]
emp_ages = [age_pool[i % len(age_pool)] for i in range(100)]

city_pool = ["london", "London", "LONDON", "paris", "Paris", "  PARIS", "tokyo", "Tokyo", "new york", "  NEW YORK  "]
emp_cities = [city_pool[i % len(city_pool)] for i in range(100)]

dept_pool = ["Tech", "tech", "TECH", "hr", "HR", "  HR  ", "sales", "Sales", "SALES", "Marketing"]
emp_depts = [dept_pool[i % len(dept_pool)] for i in range(100)]

remote_pool = ["Home", "home", "HOME", "office", "Office", "  OFFICE", "hybrid", "Hybrid", "HYBRID", "Home"]
emp_remote = [remote_pool[i % len(remote_pool)] for i in range(100)]

exp_pool = [7, np.nan, 2, 15, 22, 1, np.nan, 9, 5, 12, 24, 4, 11, 88, 16, 2, 10, np.nan, 21, 95]
emp_exps = [exp_pool[i % len(exp_pool)] for i in range(100)]

sal_pool = [64000, 71000, 48000, np.nan, 105000, 39000, 58000, 82000, 61000, 89000]
emp_sals = [sal_pool[i % len(sal_pool)] if i % 7 != 0 else np.nan for i in range(100)]

dirty_data = {
    "Emp_ID": emp_ids,
    "Emp_Name": emp_names,
    "Age": emp_ages,
    "City": emp_cities,
    "Department": emp_depts,
    "Remote_Status": emp_remote,
    "Experience_Years": emp_exps,
    "Salary_USD": emp_sals
}

df_Dirty= pd.DataFrame(dirty_data)

print("100-Row Dataset Loaded")
print(df_Dirty.shape)
print(df_Dirty.head())


print(df_Dirty)

print(df_Dirty.info())


df_Dirty.loc[df_Dirty['Age']>60,'Age']=np.nan

print(df_Dirty['Age'])


df_Dirty.loc[df_Dirty['Age']<18,'Age']=np.nan

print(df_Dirty.info())





df_Dirty['Age']=df_Dirty['Age'].fillna(df_Dirty['Age'].median())

print(df_Dirty.info())


print(df_Dirty.head(60))


df_Dirty['Age']=df_Dirty['Age'].astype(int)


print(df_Dirty.head(60))



df_Dirty['City']=df_Dirty['City'].str.strip().str.upper()


print(df_Dirty.head(60))




df_Dirty['Department']=df_Dirty['Department'].str.strip().str.upper()


print(df_Dirty.head(60))




df_Dirty['Remote_Status']=df_Dirty['Remote_Status'].str.strip().str.upper()


print(df_Dirty.head(60))



df_Dirty.loc[df_Dirty['Experience_Years']>60,'Experience_Years']=np.nan

print(df_Dirty.head(60))



df_Dirty['Experience_Years']=df_Dirty['Experience_Years'].fillna(df_Dirty['Experience_Years'].median())

print(df_Dirty.head(60))



df_Dirty['Experience_Years']=df_Dirty['Experience_Years'].astype(int)

print(df_Dirty.head(60))




df_Dirty['Salary_USD']=df_Dirty['Salary_USD'].fillna(df_Dirty['Salary_USD'].median())


print(df_Dirty.head(60))



df_Dirty['Salary_USD']=df_Dirty['Salary_USD'].astype(int)



print(df_Dirty.head(60))



print(df_Dirty.info())


df_Dirty=pd.get_dummies(df_Dirty,columns=['City'],dtype=int)

print(df_Dirty.head(60))



df_Dirty=pd.get_dummies(df_Dirty,columns=['Department'],dtype=int)

print(df_Dirty.head(60))



df_Dirty=pd.get_dummies(df_Dirty,columns=['Remote_Status'],dtype=int)

print(df_Dirty.head(60))


df_Dirty=df_Dirty.drop_duplicates()

print(df_Dirty.head(60))


df_Dirty.to_csv('Dataset temp 7 cleaning.csv',index=False)




# i'm busy so this is temp Dateset i clean :)

# i'm so happy :)
# this is bigning :) (To Be Best Ai Engineer :)...)