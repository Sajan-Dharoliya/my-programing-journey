import numpy as np
import pandas as pd

# Global E-Commerce Advanced Dataset - Version 8 (MNC Suite)
advanced_data = {
    "Employee_ID": [901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
                    921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940],
    
    "Emp_Name": ["Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander",
                 "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Sebastian", "Mateo",
                 "Jack", "Owen", "Theodore", "Aiden", "Samuel", "Joseph", "John", "David", "Wyatt", "Matthew",
                 "Luke", "Asher", "Carter", "Julian", "Grayson", "Leo", "Jayden", "Gabriel", "Isaac", "Lincoln"],
    
    "Birth_Year": [1992, 1985, np.nan, 2001, 1978, 1995, 2015, 1988, 1993, np.nan, 
                  1982, 1990, 2003, 1965, 1997, 1940, 1989, 1994, 2000, np.nan,
                  1986, 1991, 1996, 1983, 1975, 2002, 1998, 1987, 1992, 1990,
                  1979, 1984, np.nan, 1999, 1993, 1988, 2005, 1972, 1996, 1991],
    
    "Country": ["USA", "uk", "  USA  ", "Canada", "usa", "UK", "CANADA", "Germany", "germany", np.nan,
                "USA", "Canada", "UK", "Germany", "France", "france", "FRANCE", "USA", "UK", "Canada",
                "USA", "UK", "Canada", "Germany", "France", "USA", "UK", "Canada", "Germany", np.nan,
                "USA", "UK", "Canada", "Germany", "France", "USA", "UK", "Canada", "Germany", "France"],
    
    "Performance_Rating": ["Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Medium",
                          "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High",
                          "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low",
                          "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium"],
    
    "Department": ["Tech", "HR", "Sales", "Tech", "HR", "Sales", "Tech", "HR", "Sales", "Tech",
                   "HR", "Sales", "Tech", "HR", "Sales", "Tech", "HR", "Sales", "Tech", np.nan,
                   "Tech", "HR", "Sales", "Tech", "HR", "Sales", "Tech", "HR", "Sales", "Tech",
                   "HR", "Sales", "Tech", "HR", "Sales", "Tech", "HR", "Sales", "Tech", "HR"],
    
    "Salary_USD": ["55000", "62000", "75000", "48000", "69000", "81000", "43000", "58000", "72000", "65000",
                  "83000", "51000", "60000", "95000", "46000", "70000", "88000", "53000", "64000", "77000",
                  "59000", "63000", "76000", "49000", "71000", "82000", "45000", "57000", "73000", "66000",
                  "84000", "52000", "61000", "96000", "47000", "71000", "89000", "54000", "65000", "78000"]
}

df_adv = pd.DataFrame(advanced_data)
print("--- 🚨 Advanced MNC Dataset Loaded (40 Rows)! ---")
print(df_adv.head())


print(df_adv)




print(df_adv.info())



print(df_adv.describe())

print(df_adv['Salary_USD'].dtype)


df_adv['Salary_USD']=df_adv['Salary_USD'].astype(int)

print(df_adv['Salary_USD'].dtype)


print(df_adv.describe())



print(df_adv)




df_adv['Birth_Year']=df_adv['Birth_Year'].fillna(df_adv['Birth_Year'].median())


print(df_adv)

df_adv['Birth_Year']=df_adv['Birth_Year'].astype(int)

print(df_adv['Birth_Year'].dtype)




print(df_adv)

df_adv['Age']=2026-df_adv['Birth_Year']

print(df_adv)



df_adv.loc[6,'Age']=np.nan

print(df_adv)



df_adv.loc[df_adv['Age']>60,'Age']=np.nan

print(df_adv)




df_adv.loc[df_adv['Birth_Year']<1966,'Birth_Year']=np.nan


print(df_adv)


df_adv.loc[df_adv['Birth_Year']>2014,'Birth_Year']=np.nan

print(df_adv)


df_adv['Birth_Year']=df_adv['Birth_Year'].fillna(df_adv['Birth_Year'].median())

df_adv['Age']=df_adv['Age']=2026-df_adv['Birth_Year']

print(df_adv)


df_adv['Age']=df_adv['Age'].astype(int)

print(df_adv)



df_adv['Birth_Year']=df_adv['Birth_Year'].astype(int)


print(df_adv)


df_adv['Country']=df_adv['Country'].fillna('USA')


print(df_adv)


df_adv['Country']=df_adv['Country'].str.strip().str.upper()


print(df_adv)




Performance_Rule={'Low':0,'Medium':1,'High':2}



df_adv['Performance_Rating']=df_adv['Performance_Rating'].map(Performance_Rule)



print(df_adv)


df_adv.loc[19,'Department']='Tech'

print(df_adv)


df_adv=pd.get_dummies(df_adv,columns=['Department'],dtype=int)



print(df_adv)


df_adv=df_adv.drop_duplicates()

print(df_adv)


df_adv.to_csv('Dataset 7 cleaning.csv',index=False)


# i'm so happy :)
# this is bigning :) (To Be Best Ai Engineer :)...)