import numpy as np
import pandas as pd
import random

# Seed set
np.random.seed(42)
random.seed(42)

num_rows = 1000

# 1. Base Data Generate
emp_ids = list(range(1001, 1001 + num_rows))
names = ["Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander",
         "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Sebastian", "Mateo",
         "Jack", "Owen", "Theodore", "Aiden", "Samuel", "Joseph", "John", "David", "Wyatt", "Matthew",
         "Luke", "Asher", "Carter", "Julian", "Grayson", "Leo", "Jayden", "Gabriel", "Isaac", "Lincoln"]
emp_names = [random.choice(names) for _ in range(num_rows)]


birth_years = np.random.randint(1970, 2005, size=num_rows).astype(float)


countries = ["USA", "uk", "  USA  ", "Canada", "usa", "UK", "CANADA", "Germany", "germany", "France", "france", "FRANCE", "India", "india", "INDIA"]
emp_countries = [random.choice(countries) for _ in range(num_rows)]

# Departments
deps = ["Tech", "HR", "Sales", "Marketing", "Finance"]
emp_deps = [random.choice(deps) for _ in range(num_rows)]


experience = np.random.randint(0, 26, size=num_rows).astype(float)

# Performance
ratings = ["Low", "Medium", "High"]
emp_ratings = [random.choice(ratings) for _ in range(num_rows)]

salaries = 30000 + (experience * 2200) + (np.random.randint(5000, 15000, size=num_rows))
for i in range(num_rows):
    if emp_ratings[i] == "High": salaries[i] += 10000
    elif emp_ratings[i] == "Medium": salaries[i] += 5000


emp_salaries = [str(int(s)) for s in salaries]


for i in range(num_rows):

    if i % 15 == 0: birth_years[i] = np.nan
    if i % 22 == 0: emp_countries[i] = None  
    if i % 18 == 0: emp_deps[i] = None
    if i % 25 == 0: experience[i] = np.nan
    

    if i == 50: birth_years[i] = 1935 
    if i == 150: birth_years[i] = 2021
    if i == 250: experience[i] = 85    

df_mega_dataset = pd.DataFrame({
    "Employee_ID": emp_ids,
    "Emp_Name": emp_names,
    "Birth_Year": birth_years,
    "Country": emp_countries,
    "Department": emp_deps,
    "Experience_Years": experience,
    "Performance_Rating": emp_ratings,
    "Salary_USD": emp_salaries
})

# 4. CSV File Save 
df_mega_dataset.to_csv("Mega_Employee_Dataset_1000.csv", index=False)
print("--- 🔥 BOOM! 1000 Rows Ka Complex Dataset Taiyar Ho Gaya! ---")
print(f"Shape of Dataset: {df_mega_dataset.shape}")
print("\n--- Pehli 5 rows dekh lo: ---")
print(df_mega_dataset.head())

print(df_mega_dataset)



mega_dataset=pd.read_csv('Mega_Employee_Dataset_1000.csv')

print(df_mega_dataset)





print(df_mega_dataset.info())


print(df_mega_dataset.describe())


df_mega_dataset['Salary_USD']=df_mega_dataset['Salary_USD'].astype(int)



print(df_mega_dataset.describe().astype(int))


df_mega_dataset.loc[df_mega_dataset['Birth_Year']<1966]=np.nan

print(df_mega_dataset.info())

df_mega_dataset.loc[df_mega_dataset['Birth_Year']>2021,'Birth_Year']=np.nan

print(df_mega_dataset.info())

print(df_mega_dataset.head())


print(df_mega_dataset.isnull().sum())

df_mega_dataset['Age']=2026-df_mega_dataset['Birth_Year']

print(df_mega_dataset.head())


print(df_mega_dataset.info())


df_mega_dataset.loc[df_mega_dataset['Age']>60,'Age']=np.nan

print(df_mega_dataset.head())

print(df_mega_dataset.info())

print(df_mega_dataset.describe())




print(df_mega_dataset.info())


df_mega_dataset.loc[df_mega_dataset['Age']<18,'Age']=np.nan


print(df_mega_dataset.info())




print(df_mega_dataset.tail())


print(df_mega_dataset.isnull().sum())


df_mega_dataset['Age']=df_mega_dataset['Age'].fillna(df_mega_dataset['Age'].median())

print(df_mega_dataset.isnull().sum())



df_mega_dataset['Birth_Year']=df_mega_dataset['Birth_Year'].fillna(df_mega_dataset['Birth_Year'].median())


print(df_mega_dataset.isnull().sum())



print(df_mega_dataset.head(30))

print(df_mega_dataset.tail(30))




df_mega_dataset['Birth_Year']=df_mega_dataset['Birth_Year'].astype(int)


print(df_mega_dataset['Birth_Year'].dtype)



print(df_mega_dataset.info())



df_mega_dataset['Age']=df_mega_dataset['Age'].astype(int)


print(df_mega_dataset['Age'].dtype)

print(df_mega_dataset.info())

df_mega_dataset['Experience_Years']=df_mega_dataset['Experience_Years'].fillna(df_mega_dataset['Experience_Years'].median())


print(df_mega_dataset.info())



print(df_mega_dataset.head(30))

print(df_mega_dataset.tail(30))


df_mega_dataset['Experience_Years']=df_mega_dataset['Experience_Years'].astype(int)

print(df_mega_dataset['Experience_Years'].dtype)



df_mega_dataset['Performance_Rating']=df_mega_dataset['Performance_Rating'].fillna('High')


print(df_mega_dataset.info())


Performance_Rule={'Low':0,'Medium':1,'High':2}

df_mega_dataset['Performance_Rating']=df_mega_dataset['Performance_Rating'].map(Performance_Rule)


print(df_mega_dataset.head(30))



df_mega_dataset['Country']=df_mega_dataset['Country'].fillna('USA')

print(df_mega_dataset.head(30))


df_mega_dataset['Country']=df_mega_dataset['Country'].str.strip().str.upper()




print(df_mega_dataset.head(30))



print(df_mega_dataset.tail(30))



df_mega_dataset['Department']=df_mega_dataset['Department'].fillna('Tech')


print(df_mega_dataset.head(30))




df_mega_dataset=df_mega_dataset.drop(columns='Age')



print(df_mega_dataset.head(30))



df_mega_dataset['Age']=2026-df_mega_dataset['Birth_Year']

print(df_mega_dataset.head(30))



print(df_mega_dataset.isnull().sum())



df_mega_dataset['Salary_USD']=df_mega_dataset['Salary_USD'].fillna(df_mega_dataset['Salary_USD'].median())


print(df_mega_dataset.isnull().sum())



df_mega_dataset['Emp_Name']=df_mega_dataset['Emp_Name'].fillna('Martinez')

print(df_mega_dataset.isnull().sum())




df_mega_dataset['Employee_ID']=df_mega_dataset['Employee_ID'].fillna(df_mega_dataset['Employee_ID'].median())

print(df_mega_dataset.isnull().sum())




print(df_mega_dataset.head(30))



df_mega_dataset['Employee_ID']=df_mega_dataset['Employee_ID'].astype(int)


print(df_mega_dataset['Employee_ID'].dtype)



print(df_mega_dataset.info())


df_mega_dataset['Salary_USD']=df_mega_dataset['Salary_USD'].astype(int)



print(df_mega_dataset['Salary_USD'].dtype)



print(df_mega_dataset.info())





print(df_mega_dataset.head(30))




df_mega_dataset=pd.get_dummies(df_mega_dataset,columns=['Department'],dtype=int)


print(df_mega_dataset.head(30))


df_mega_dataset=pd.get_dummies(df_mega_dataset,columns=['Country'],dtype=int)


print(df_mega_dataset.head(30))


df_mega_dataset=df_mega_dataset.drop_duplicates()


print(df_mega_dataset.info())


df_mega_dataset.to_csv('Dataset 8 cleaning.csv',index=False)



# i'm so happpy :)
# this is bigning :) (To Be Best Ai Engineer :)...)