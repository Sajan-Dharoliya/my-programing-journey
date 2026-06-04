import numpy as np
import pandas as pd


dirty_data = {
    "Emp_ID": list(range(701, 761)),
    
    "Emp_Name": ["John", "Emily", "Michael", "Jessica", "David", "Sarah", "James", "Karen", "Robert", "Lisa",
                 "William", "Nancy", "Daniel", "Betty", "Matthew", "Sandra", "Anthony", "Ashley", "Mark", "Dorothy",
                 "Donald", "Kimberly", "Steven", "Emily", "Paul", "Donna", "Andrew", "Michelle", "Joshua", "Carol",
                 "Kevin", "Amanda", "Brian", "Melissa", "George", "Deborah", "Edward", "Stephanie", "Ronald", "Rebecca",
                 "Timothy", "Sharon", "Jason", "Cynthia", "Jeffrey", "Kathleen", "Gary", "Shirley", "Ryan", "Amy",
                 "Nicholas", "Angela", "Eric", "Anna", "Stephen", "Ruth", "Jacob", "Brenda", "Larry", "Pamela"],
    
    "Age": [28, 35, np.nan, 42, 22, 31, 55, np.nan, 12, 40,
            33, 48, 26, np.nan, 62, 29, 37, 110, 45, 23,
            np.nan, 34, 50, 16, 27, 41, np.nan, 38, 49, 32,
            43, np.nan, 25, 39, 58, 21, np.nan, 47, 30, 53,
            14, 36, np.nan, 51, 29, 44, 115, np.nan, 33, 26,
            40, 52, np.nan, 31, 45, 22, np.nan, 57, 35, 48],
            
    "City": ["new york", "  NEW YORK  ", "london", "London", "LONDON", "paris", "Paris", "  PARIS", "tokyo", "Tokyo",
             "new york", "London", "paris", "Tokyo", "berlin", "Berlin", "new york", "London", "paris", "Tokyo",
             "BERLIN", "  LONDON", "Paris", "Tokyo", "Berlin", "new york", "London", "paris", "Tokyo", "Berlin",
             "new york", "London", "  PARIS", "Tokyo", "Berlin", "new york", "London", "paris", "Tokyo", "berlin",
             "NEW YORK", "London", "paris", "Tokyo", "Berlin", "new york", "  LONDON", "paris", "Tokyo", "Berlin",
             "new york", "London", "paris", "Tokyo", "BERLIN", "new york", "London", "paris", "Tokyo", "Berlin"],
             
    "Experience_Years": [5, 12, 8, np.nan, 1, 7, 25, 14, np.nan, 15,
                         9, 20, 3, 11, np.nan, 6, 13, 85, 18, 2,
                         10, np.nan, 22, 0, 4, 16, np.nan, 11, 21, 8,
                         16, 11, np.nan, 13, 32, 1, 5, np.nan, 7, 24,
                         np.nan, 10, 4, 23, 6, 15, 90, 12, np.nan, 3,
                         14, 26, 8, np.nan, 17, 2, 9, 28, np.nan, 19],
                        
    "Salary_USD": [55000, 82000, 68000, np.nan, 41000, 62000, 115000, 89000, 15000, 78000,
                  73000, 98000, 49000, 66000, np.nan, 59000, 74000, 120000, 85000, 45000,
                  77000, np.nan, 102000, 38000, 51000, 81000, np.nan, 69000, 94000, 63000,
                  88000, 72000, np.nan, 79000, 135000, 42000, 53000, 92000, 58000, 108000,
                  32000, 70000, np.nan, 105000, 60000, 84000, 140000, 75000, np.nan, 47000,
                  80000, 118000, 67000, np.nan, 90000, 44000, 71000, 125000, np.nan, 87000]
}

df_Dirty = pd.DataFrame(dirty_data)


print("Mega Dataset Loaded (60 Rows)")
print(df_Dirty.head())


print(df_Dirty)



print(df_Dirty.info())




df_Dirty.loc[df_Dirty['Age']>100,'Age']=np.nan

print(df_Dirty)

df_Dirty.loc[df_Dirty['Age']<18,'Age']=np.nan

print(df_Dirty.info())

print(df_Dirty)



df_Dirty['Age']=df_Dirty['Age'].fillna(df_Dirty['Age'].median())


print(df_Dirty)

df_Dirty['Age']=df_Dirty['Age'].astype(int)

print(df_Dirty)




df_Dirty['City']=df_Dirty['City'].str.strip().str.upper()


print(df_Dirty)



df_Dirty.loc[df_Dirty['Experience_Years']>60,'Experience_Years']=np.nan


print(df_Dirty)


df_Dirty['Experience_Years']=df_Dirty['Experience_Years'].fillna(df_Dirty['Experience_Years'].median())



print(df_Dirty)

df_Dirty['Experience_Years']=df_Dirty['Experience_Years'].astype(int)



print(df_Dirty['Experience_Years'].dtype)


print(df_Dirty)




df_Dirty['Salary_USD']=df_Dirty['Salary_USD'].fillna(df_Dirty['Salary_USD'].median())


print(df_Dirty)



df_Dirty['Salary_USD']=df_Dirty['Salary_USD'].astype(int)


print(df_Dirty['Salary_USD'].dtype)

print(df_Dirty)




df_Dirty=pd.get_dummies(df_Dirty,columns=['City'],dtype=int)


print(df_Dirty)





df_Dirty=df_Dirty.drop_duplicates()


print(df_Dirty)


df_Dirty.to_csv('Dataset temp 4 cleaning.csv',index=False)



print(df_Dirty)




# i'm busy so this is temp Dateset i clean :)

# i'm so happy :)
# this is bigning :) (To Be Best Ai Engineer :)...)