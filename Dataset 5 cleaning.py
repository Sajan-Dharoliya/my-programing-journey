import numpy as np
import pandas as pd

# Global E-Commerce Dataset - Version 6 (Pure International Edition)
international_data = {
    "Customer_ID": [701, 702, 703, 704, 705, 706, 707, 701, 708, 709, 
                    710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 
                    720, 721, 722, 723, 724, 725, 726, 727, 728, 729],
    
    "Customer_Name": ["James Smith", "Emma Johnson", "Oliver Brown", "Sophia Davis", "William Miller", 
                     "Isabella Wilson", "Lucas Moore", "James Smith", "Mia Taylor", "Alexander Anderson",
                     "Charlotte Thomas", "Ethan Jackson", "Amelia White", "Mason Harris", "Evelyn Martin",
                     "Logan Thompson", "Harper Garcia", "Benjamin Martinez", "Elijah Robinson", "Emily Clark",
                     "James Smith", "Aria Rodriguez", "Jacob Lewis", "Elizabeth Lee", "Michael Walker",
                     "Avery Hall", "Ethan Jackson", "Sofia Allen", "Daniel Young", "Madison King"],
    
    "Age": [34.0, np.nan, 28.0, 45.0, -12.0, 56.0, 140.0, 34.0, 23.0, np.nan, 
            31.0, 48.0, 110.0, 22.0, 29.0, 52.0, -3.0, 38.0, 41.0, 26.0, 
            34.0, 47.0, 33.0, np.nan, 50.0, 19.0, 48.0, 30.0, 61.0, 25.0],
    
    "City": ["New York", "London", "Los Angeles", "New York", "Miami", 
             "Paris", "Tokyo", "New York", "Sydney", np.nan, 
             "Chicago", "Toronto", "New York", "London", "Los Angeles",
             "Miami", "Paris", "Tokyo", "Sydney", "Chicago",
             "New York", np.nan, "Los Angeles", "London", "Miami",
             "Paris", "Toronto", "Tokyo", "Sydney", "Chicago"],
    
    "Customer_Segment": ["Silver", "Gold", "Platinum", "Silver", "Gold", 
                        "Platinum", "Silver", "Silver", "Gold", "Platinum",
                        "Silver", "Gold", "Platinum", "Silver", "Gold",
                        "Platinum", "Silver", "Gold", "Platinum", "Silver",
                        "Silver", "Platinum", "Silver", "Gold", "Platinum",
                        "Silver", "Gold", "Platinum", "Silver", "Gold"],
    
    "Product": ["Laptop", "Smartphone", "Watch", "Laptop", "Earphones", 
                "Tablet", "Laptop", "Laptop", "Smartwatch", "Trimmer",
                np.nan, "Speakers", "Router", "Watch", "Earphones",
                "Smartphone", "Tablet", np.nan, "Laptop", "Smartwatch",
                "Laptop", "Speakers", "Router", "Watch", "Earphones",
                "Smartphone", "Tablet", "Laptop", "Smartwatch", "Trimmer"],
    
    "Price": [1200, 800, 350, 1200, 45, "150", 1100, 1200, 250, 40,
              600, 95, 55, 320, 35, "850", 180, 120, 1050, 220,
              1200, 110, 60, 340, 50, 799, 190, 999, 210, 45],
    
    "Purchase_Date": ["2026-05-01", "2026-05-02", "2026-05-03", "2026-05-01", "2026-05-05", 
                     np.nan, "2026-05-07", "2026-05-01", "2026-05-09", "2026-05-10", 
                     "2026-05-11", "2026-05-12", "2026-05-13", "2026-05-14", "2026-05-15",
                     "2026-05-16", "2026-05-17", "2026-05-18", "2026-05-19", "2026-05-20",
                     "2026-05-01", "2026-05-22", "2026-05-23", "2026-05-24", "2026-05-25",
                     "2026-05-26", "2026-05-27", "2026-05-28", "2026-05-29", "2026-05-30"]
}

df_international = pd.DataFrame(international_data)
print("--- 🌍 Pure International Dataset Loaded! ---")
print(df_international.head())

print(df_international)




print(df_international.info())


print(df_international.describe())


df_international['Price']=df_international['Price'].astype(int)

print(df_international)


print(df_international.describe())


print(df_international)


df_international.loc[4,'Age']=12

print(df_international)



df_international.loc[df_international['Age']>100,'Age']=np.nan

print(df_international)




df_international.loc[16,'Age']=np.nan

print(df_international)


df_international['Age']=df_international['Age'].fillna(df_international['Age'].median())


print(df_international)



df_international.loc[9,'City']='California'

print(df_international)


df_international.loc[21,'City']='Florida'

print(df_international)


segment_rule={'Silver':0,'Gold':1,'Platinum':2}



df_international['Customer_Segment']=df_international['Customer_Segment'].map(segment_rule)


print(df_international[['Customer_Name','Customer_Segment']].head())




print(df_international)



df_international.loc[10,'Product']='Monitor'


print(df_international)



df_international.loc[17,'Product']='Headphone'


print(df_international)



df_international['Purchase_Date']=df_international['Purchase_Date'].fillna('2026-05-04')


print(df_international['Purchase_Date'].dtype)


print(df_international)



df_international['Purchase_Date']=pd.to_datetime(df_international['Purchase_Date'])



print(df_international['Purchase_Date'].dtype)


print(df_international)




df_international=df_international.sort_values(by='Purchase_Date',ascending=True)



print(df_international)




df_international['Age']=df_international['Age'].astype(int)


print(df_international)


df_international=df_international.drop_duplicates()

# this is bigning :)
# i'm so Happy :) (To BE Best Ai Engineer In Real :)))....)