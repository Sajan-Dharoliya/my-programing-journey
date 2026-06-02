import numpy as np
import pandas as pd


dirty_data = {
    "Property_ID": list(range(4001, 4031)),
    
    "Owner_Name": ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth",
                   "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen",
                   "Christopher", "Nancy", "Daniel", "Lisa", "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra"],
    
    "Property_Size_SqFt": [1200, 2500, np.nan, 1800, 950, 3100, 1500, np.nan, 2200, 45000,
                           1350, 2800, 850, np.nan, 1900, 2400, 1100, -400, 1750, np.nan,
                           3200, 1400, 900, np.nan, 2100, 2700, 1650, np.nan, 2300, 1300],
                           
    "City": ["new york", "  NEW YORK  ", "london", "London", "LONDON", "paris", "Paris", "  PARIS", "tokyo", "Tokyo",
             "new york", "London", "paris", "Tokyo", "berlin", "Berlin", "new york", "London", "paris", "Tokyo",
             "BERLIN", "  LONDON", "Paris", "Tokyo", "Berlin", "new york", "London", "paris", "Tokyo", "Berlin"],
             
    "Price_USD": ["$450000", "$850000", "$320000", np.nan, "$250000", "$990000", "$510000", "$720000", np.nan, "$1500000",
                  "$410000", "$890000", "$210000", "$630000", np.nan, "$790000", "$380000", "$550000", "$610000", np.nan,
                  "$1100000", "$480000", "$230000", "$820000", "$950000", np.nan, "$530000", "$870000", "$740000", "$420000"]
}

df_dirty = pd.DataFrame(dirty_data)

print("Dataset Loaded (30 Rows)")
print(df_dirty.head())




print(df_dirty)


df_dirty.loc[9,'Property_Size_SqFt']=np.nan

df_dirty.loc[17,'Property_Size_SqFt']=np.nan


df_dirty['Property_Size_SqFt']=df_dirty['Property_Size_SqFt'].fillna(df_dirty['Property_Size_SqFt'].median())


print(df_dirty)





df_dirty['Property_Size_SqFt']=df_dirty['Property_Size_SqFt'].astype(int)



df_dirty['City']=df_dirty['City'].str.strip().str.upper()

print(df_dirty)



df_dirty['Price_USD']=df_dirty['Price_USD'].str.replace('$','',regex=False)

print(df_dirty)


df_dirty['Price_USD']=df_dirty['Price_USD'].astype(float)


df_dirty['Price_USD']=df_dirty['Price_USD'].fillna(df_dirty['Price_USD'].median())


df_dirty['Price_USD']=df_dirty['Price_USD'].astype(int)



print(df_dirty['Price_USD'].dtype)

print(df_dirty)



df_dirty=pd.get_dummies(df_dirty,columns=['City'],dtype=int)


df_dirty=df_dirty.drop_duplicates()

print(df_dirty)


df_dirty.to_csv('Dataset temp 2 cleaning.csv',index=False)

# i'm busy so this is temp Dateset i clean :)

# i'm so happy :)
# this is bigning :) (To Be Best Ai Engineer :)...)