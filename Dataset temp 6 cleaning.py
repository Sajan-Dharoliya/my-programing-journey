import numpy as np
import pandas as pd



dirty_data = {
    "Emp_ID": list(range(901, 981)),
    
    "Emp_Name": ["Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander",
                 "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Sebastian", "Mateo",
                 "Jack", "Owen", "Theodore", "Aiden", "Samuel", "Joseph", "John", "David", "Wyatt", "Matthew",
                 "Luke", "Asher", "Carter", "Julian", "Grayson", "Leo", "Jayden", "Gabriel", "Isaac", "Lincoln",
                 "Anthony", "Dylan", "Leo", "Jaxon", "Lincoln", "Christopher", "Andrew", "Theodore", "Caleb", "Ryan",
                 "Asher", "Nathan", "Thomas", "Leo", "Isaiah", "Charles", "Josiah", "Hudson", "Christian", "Hunter",
                 "Jonathan", "Connor", "Isaiah", "Charles", "Josiah", "Hudson", "Christian", "Hunter", "Eli", "Ezra",
                 "Aaron", "Adrian", "Maverick", "Ismael", "Colten", "Jaden", "Gavin", "Jasper", "Weston", "Silas"],
    
    "Age": [31, np.nan, 24, 45, 50, 19, np.nan, 33, 28, 41,
            62, 29, 37, 112, 45, 23, np.nan, 34, 52, 15,
            27, 42, np.nan, 38, 49, 32, 43, np.nan, 25, 39,
            58, 21, np.nan, 47, 30, 53, 13, 36, np.nan, 51,
            29, 44, 118, np.nan, 33, 26, 40, 55, np.nan, 31,
            46, 22, np.nan, 57, 35, 48, 30, np.nan, 24, 43,
            34, np.nan, 28, 41, 52, 16, np.nan, 38, 49, 32,
            43, np.nan, 25, 39, 114, 21, np.nan, 47, 30, 53],
            
    "City": ["london", "London", "LONDON", "paris", "Paris", "  PARIS", "tokyo", "Tokyo", "new york", "  NEW YORK  ",
             "london", "Paris", "Tokyo", "berlin", "Berlin", "new york", "London", "paris", "Tokyo", "berlin",
             "NEW YORK", "London", "paris", "Tokyo", "Berlin", "new york", "  LONDON", "paris", "Tokyo", "Berlin",
             "new york", "London", "paris", "Tokyo", "BERLIN", "new york", "London", "paris", "Tokyo", "Berlin",
             "london", "London", "LONDON", "paris", "Paris", "  PARIS", "tokyo", "Tokyo", "new york", "  NEW YORK  ",
             "london", "Paris", "Tokyo", "berlin", "Berlin", "new york", "London", "paris", "Tokyo", "berlin",
             "NEW YORK", "London", "paris", "Tokyo", "Berlin", "new york", "  LONDON", "paris", "Tokyo", "Berlin",
             "new york", "London", "paris", "Tokyo", "BERLIN", "new york", "London", "paris", "Tokyo", "Berlin"],
             
    "Department": ["Tech", "tech", "TECH", "hr", "HR", "  HR  ", "sales", "Sales", "SALES", "Marketing",
                   "Tech", "HR", "Sales", "marketing", "Marketing", "Tech", "HR", "Sales", "Marketing", "Finance",
                   "finance", "FINANCE", "Tech", "HR", "Sales", "Marketing", "Finance", "Tech", "HR", "Sales",
                   "Tech", "tech", "TECH", "hr", "HR", "  HR  ", "sales", "Sales", "SALES", "Marketing",
                   "Tech", "HR", "Sales", "marketing", "Marketing", "Tech", "HR", "Sales", "Marketing", "Finance",
                   "finance", "FINANCE", "Tech", "HR", "Sales", "Marketing", "Finance", "Tech", "HR", "Sales",
                   "Tech", "HR", "Sales", "Marketing", "Finance", "Tech", "HR", "Sales", "Marketing", "Finance",
                   "Tech", "tech", "TECH", "hr", "HR", "  HR  ", "sales", "Sales", "SALES", "Marketing"],

    "Remote_Status": ["Home", "home", "HOME", "office", "Office", "  OFFICE", "hybrid", "Hybrid", "HYBRID", "Home",
                      "Office", "Hybrid", "home", "Home", "Office", "Hybrid", "Home", "Office", "Hybrid", "home",
                      "Office", "Hybrid", "Home", "Office", "Hybrid", "home", "Office", "Hybrid", "Home", "Office",
                      "Hybrid", "home", "Office", "Hybrid", "Home", "Office", "Hybrid", "home", "Office", "Hybrid",
                      "Home", "home", "HOME", "office", "Office", "  OFFICE", "hybrid", "Hybrid", "HYBRID", "Home",
                      "Office", "Hybrid", "home", "Home", "Office", "Hybrid", "Home", "Office", "Hybrid", "home",
                      "Office", "Hybrid", "Home", "Office", "Hybrid", "home", "Office", "Hybrid", "Home", "Office",
                      "Hybrid", "home", "Office", "Hybrid", "Home", "Office", "Hybrid", "home", "Office", "Hybrid"],
             
    "Experience_Years": [7, np.nan, 2, 15, 22, 1, np.nan, 9, 5, 12,
                         24, 4, 11, 88, 16, 2, 10, np.nan, 21, 0,
                         4, 14, np.nan, 10, 23, 8, 13, np.nan, 3, 11,
                         27, 1, np.nan, 18, 6, 20, 95, 8, np.nan, 21,
                         5, 13, 9, np.nan, 7, 2, 12, 25, np.nan, 6,
                         17, 0, np.nan, 26, 8, 19, 4, np.nan, 1, 14,
                         10, np.nan, 5, 12, 23, 1, np.nan, 14, 22, 7,
                         13, 1, np.nan, 18, 99, 3, np.nan, 20, 6, 15],
                        
    "Salary_USD": [64000, 71000, 48000, np.nan, 105000, 39000, 58000, 82000, 61000, 89000,
                   112000, 54000, 81000, 130000, 87000, 46000, 76000, np.nan, 101000, 35000,
                   52000, 79000, np.nan, 72000, 104000, 68000, 86000, 74000, np.nan, 80000,
                   121000, 40000, np.nan, 92000, 59000, 108000, 140000, 65000, np.nan, 103000,
                   57000, 83000, 69000, np.nan, 73000, 47000, 88000, 118000, np.nan, 66000,
                   95000, 38000, np.nan, 123000, 67000, 91000, 53000, 78000, np.nan, 84000,
                   76000, 68000, np.nan, 89000, 115000, 42000, 59000, 92000, 104000, 65000,
                   85000, 39000, np.nan, 90000, 145000, 48000, np.nan, 101000, 60000, 88000]
}

df_dirty = pd.DataFrame(dirty_data)


print("80-Row Mega Dataset Loaded ---")
print(df_dirty.head())


print(df_dirty.head(60))


print(df_dirty.info())



df_dirty.loc[df_dirty['Age']>100,'Age']=np.nan

df_dirty.loc[df_dirty['Age']<18,'Age']=np.nan

print(df_dirty.info())


df_dirty['Age']=df_dirty['Age'].fillna(df_dirty['Age'].median())

print(df_dirty.head(60))



print(df_dirty.info())


print(df_dirty.head(60))

df_dirty['Age']=df_dirty['Age'].astype(int)


print(df_dirty['Age'].dtype)


print(df_dirty.head(60))



df_dirty['City']=df_dirty['City'].str.strip().str.upper()

print(df_dirty.head(60))


df_dirty['Department']=df_dirty['Department'].str.strip().str.upper()

print(df_dirty.head(60))


df_dirty['Remote_Status']=df_dirty['Remote_Status'].str.strip().str.upper()

print(df_dirty.head(60))



df_dirty.loc[df_dirty['Experience_Years']>60,'Experience_Years']=np.nan

print(df_dirty.head(60))

df_dirty['Experience_Years']=df_dirty['Experience_Years'].fillna(df_dirty['Experience_Years'].median())


print(df_dirty.head(60))



df_dirty['Experience_Years']=df_dirty['Experience_Years'].astype(int)


print(df_dirty.head(60))







df_dirty['Salary_USD']=df_dirty['Salary_USD'].fillna(df_dirty['Salary_USD'].median())

print(df_dirty.head(60))



df_dirty['Salary_USD']=df_dirty['Salary_USD'].astype(int)


print(df_dirty.head(60))






df_dirty=pd.get_dummies(df_dirty,columns=['City'],dtype=int)



print(df_dirty.head(60))



df_dirty=pd.get_dummies(df_dirty,columns=['Department'],dtype=int)



print(df_dirty.head(60))




df_dirty=pd.get_dummies(df_dirty,columns=['Remote_Status'],dtype=int)



print(df_dirty.head(60))




df_dirty=df_dirty.drop_duplicates()

print(df_dirty.head(60))


df_dirty.to_csv('Dataset temp 6 cleaning.csv',index=False)


# i'm busy so this is temp Dateset i clean :)

# i'm so happy :)
# this is bigning :) (To Be Best Ai Engineer :)...)