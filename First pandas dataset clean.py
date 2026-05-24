
import numpy as np
import pandas as pd

# Global Raw Data with Errors 
global_data = {
    "Customer_ID": [501, 502, 503, 501, 504, 505, 506, 507, 502, 508, 509, 510, 511, 512, 513],
    "Customer_Name": [
        "Emma Watson", "Liam Smith", "Sofia Rossi", "Emma Watson", "Yuki Tanaka",
        "Hans Müller", "Chloe Dubois", "Lucas Silva", "Liam Smith", "Amélie Laurent",
        "Oliver Brown", "Mateo Fernandez", "Elena Petrova", "Noah Johnson", "Mia Wang"
    ],
    "Age": [29, np.nan, 31, 29, 45, -12, 24, 38, np.nan, 33, 52, 115, 27, 19, 30],
    "City": [
        "New York", "London", "Rome", "New York", "Tokyo", "Berlin", "Paris",
        "Rio", "London", np.nan, "Sydney", "Madrid", "Moscow", "Toronto", "Shanghai"
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

# DataFrame create karna
df_global = pd.DataFrame(global_data)

print("--- 🌍 Global Dataset Ready for Cleaning! ---")
print(df_global)
print(" ")


print(df_global[["Age"]])
print(df_global.isna().sum())# calculat nan 

# maza aa gaya bhai :)


print(df_global.head())

print(df_global.info())

print(df_global)

print(df_global.describe())


print(df_global.isnull().sum())


df_global['Age']=df_global['Age'].fillna(df_global['Age'].mean())
print(df_global)

print(df_global.drop_duplicates())

df_global['City']=df_global['City'].fillna('Toronto')
print(df_global)


df_global.loc[5,'Age']=12

print(df_global)

df_global.loc[df_global['Age']>100,'Age']=np.nan

df_global['Age']=df_global['Age'].fillna(df_global['Age'].mean())

print(df_global)


# df_global['Product']=df_global['Product'].fillna('Laptop')

# print(df_global)


# df_global['Product']=df_global['Product'].fillna('Earphone')

# print(df_global)



df_global.loc[6,'Product']='Earphone'

print(df_global)

df_global.loc[12,'Product']='Monitor'

print(df_global)


print(df_global.drop_duplicates())


print(df_global['Purchase_Date'].dtype)


df_global['Purchase_Date']=pd.to_datetime(df_global['Purchase_Date'])


df_global['Purchase_Date']=df_global['Purchase_Date'].fillna('2026-05-04')


df_global=df_global.sort_values(by='Purchase_Date',ascending=True)

df_global=df_global.drop_duplicates()
print(df_global)


# this is bigning :)
# i'm so happy :) 