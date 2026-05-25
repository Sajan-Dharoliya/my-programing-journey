import numpy as np
import pandas as pd

# Clean American Style Dataset with Data Bugs
global_data = {
    "Customer_ID": [501, 502, 503, 501, 504, 505, 506, 507, 502, 508, 509, 510, 511, 512, 513],
    "Customer_Name": [
        "Alex Jones", "Steve Smith", "Emma Watson", "Alex Jones", "Lily Evans",
        "John Doe", "Chris Evans", "David Miller", "Steve Smith", "Sarah Connor",
        "Tom Hardy", "Bruce Wayne", "Mary Jane", "Ryan Reynolds", "Katy Perry"
    ],
    "Age": [29, np.nan, 31, 29, 45, -12, 24, 38, np.nan, 33, 52, 115, 27, 19, 30],
    "City": [
        "New York", "Chicago", "Los Angeles", "New York", "Miami", "Boston", "Seattle",
        "Austin", "Chicago", np.nan, "Denver", "San Francisco", "Las Vegas", "Phoenix", "Houston"
    ],
    "Product": [
        "iPhone", "MacBook", "iPad", "iPhone", "AirPods", "Smartwatch", np.nan,
        "Speaker", "MacBook", "iMac", "Keyboard", "Mouse", np.nan, "Headphones", "Powerbank"
    ],
    "Price": [999, 1499, 599, 999, 249, "350", 150, 199, 1499, 1799, 129, 79, 499, "299", 49],
    "Purchase_Date": [
        "2026-05-01", "2026-05-02", "2026-05-03", "2026-05-01", "2026-05-05", np.nan,
        "2026-05-07", "2026-05-08", "2026-05-02", "2026-05-10", "2026-05-11", "2026-05-12",
        "2026-05-13", "2026-05-14", "2026-05-15"
    ]
}

# DataFrame ready karna
df_global = pd.DataFrame(global_data)

print("--- Global Dataset Ready for Practice! ---")
print(df_global)

# maza aa gaya :)
print(df_global.head())

print(df_global.info())

print(df_global.describe())

df_global['Price']=df_global['Price'].astype(int)
print(df_global)

print(df_global['Price'].dtype)

print(df_global.describe())

print(df_global)


df_global=df_global.drop_duplicates('Customer_ID')

print(df_global)



print(df_global.isnull().sum())



df_global.loc[5,'Age']=12


print(df_global)


df_global.loc[df_global['Age']>100,'Age']=np.nan


print(df_global)


df_global['Age']=df_global['Age'].fillna(df_global['Age'].median())


print(df_global)



df_global['City']=df_global['City'].fillna('California')


print(df_global)



df_global.loc[13,'City']='Florida'


print(df_global)



df_global.loc[6,'Product']='Earphone'

print(df_global)

df_global['Product']=df_global['Product'].fillna('Monitor')

print(df_global)


df_global['Purchase_Date']=df_global['Purchase_Date'].fillna('2026-05-04')

print(df_global)

print(df_global['Purchase_Date'].dtype)

df_global['Purchase_Date']=pd.to_datetime(df_global['Purchase_Date'])

print(df_global)


print(df_global['Purchase_Date'].dtype)


df_global=df_global.sort_values(by='Purchase_Date',ascending=True)

print(df_global)



df_global=df_global.sort_values(by='Customer_ID',ascending=True)


print(df_global)

# this is bigning :) 
# i'm so happy :)  (To Become Best Ai Engineer :).....)