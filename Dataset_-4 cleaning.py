import numpy as np
import pandas as pd

# Large Complex Dataset with Normal American Names & Hidden Data Bugs
ecommerce_data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 
                 1011, 1012, 1013, 1003, 1014, 1015, 1016, 1017, 1018, 1019, 
                 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029],
    
    "Customer_Name": ["James Smith", "Michael Brown", "Robert Jones", "Maria Garcia", "David Miller", 
                     "James Smith", "William Davis", "Mary Rodriguez", "Robert Jones", "Linda Martinez",
                     "Michael Brown", "David Miller", "Richard Wilson", "William Davis", "Thomas Anderson",
                     "Barbara Taylor", "Matthew Thomas", "Patricia Moore", "Jeffrey Martin", "Elizabeth Jackson",
                     "Kevin White", "Susan Harris", "Joseph Clark", "Jessica Lewis", "Michael Robinson",
                     "Sarah Walker", "Paul Young", "Karen Allen", "Timothy King", "Nancy Wright"],
    
    "Age": [28, 34, np.nan, 45, -5, 52, 120, 41, 65, np.nan, 
            39, 44, 110, np.nan, 31, 22, 29, 35, -1, 26, 
            33, 47, 28, 32, 38, 55, 23, 25, 50, 61],
    
    "City": ["New York", "Chicago", "Los Angeles", "New York", "Miami", 
             "Boston", "Seattle", "Austin", "Chicago", np.nan, 
             "San Francisco", "Las Vegas", "Phoenix", "Los Angeles", "Houston",
             "New York", "Chicago", "Los Angeles", "Miami", "Boston",
             "Seattle", np.nan, "Austin", "San Francisco", "Las Vegas",
             "Phoenix", "Houston", "Miami", "Boston", "Seattle"],
    
    "Category": ["Electronics", "Clothing", "Home", "Electronics", "Books", 
                 "Sports", "Electronics", "Books", "Home", "Clothing",
                 "Electronics", "Sports", "Home", "Home", "Books",
                 "Electronics", "Clothing", "Home", "Sports", "Books",
                 "Electronics", "Clothing", "Home", "Books", "Sports",
                 "Electronics", "Clothing", "Home", "Books", "Sports"],
    
    "Product": ["iPhone 14", "Winter Jacket", "Sofa", "iPhone 14", "Novel Pack", 
                "Football", "MacBook Pro", "Biography", "Dining Table", "Jeans",
                "Smartwatch", "Gym Kit", np.nan, "Sofa", "Comic Book",
                "AirPods", "T-Shirt", "Bed Sheets", "Tennis Racket", "Textbook",
                "Gaming PC", "Sneakers", "Curtains", "Cooking Pots", "Yoga Mat",
                "Drone", "Hoodie", "Desk Lamp", np.nan, "Running Shoes"],
    
    "Price": [999, 120, 750, 999, 45, "150", 1999, 30, 450, 80,
              299, 99, 600, 750, 25, "249", 40, 85, 110, 95,
              2500, 130, 65, 120, 55, 899, 75, 45, 199, 140],
    
    "Discount_%": [10, 5, 15, 10, 0, 20, 25, 0, 10, np.nan,
                  15, 10, 20, 15, 5, 10, 0, 12, 15, 5,
                  20, 8, 10, 0, 5, 18, 10, 0, 15, 12],
    
    "Purchase_Date": ["2026-05-01", "2026-05-02", "2026-05-03", "2026-05-01", "2026-05-05", 
                     np.nan, "2026-05-07", "2026-05-08", "2026-05-02", "2026-05-10", 
                     "2026-05-11", "2026-05-12", "2026-05-13", "2026-05-03", "2026-05-15",
                     "2026-05-16", "2026-05-17", "2026-05-18", "2026-05-19", "2026-05-20",
                     "2026-05-21", "2026-05-22", "2026-05-23", "2026-05-24", "2026-05-25",
                     "2026-05-26", "2026-05-27", "2026-05-28", "2026-05-29", "2026-05-30"]
}

df_ecommerce = pd.DataFrame(ecommerce_data)
print("--- 🛒 Large Dataset with Normal Names Loaded! ---")
print(df_ecommerce.head(10))


print(df_ecommerce)





print(df_ecommerce.info())


print(df_ecommerce.describe())



df_ecommerce['Price']=df_ecommerce['Price'].astype(int)


print(df_ecommerce.describe())


print(df_ecommerce)



df_ecommerce.loc[4,'Age']=5

print(df_ecommerce)


df_ecommerce.loc[df_ecommerce['Age']>100,'Age']=np.nan

print(df_ecommerce)



df_ecommerce.loc[df_ecommerce['Age']<0,'Age']=np.nan

print(df_ecommerce)




df_ecommerce['Age']=df_ecommerce['Age'].fillna(df_ecommerce['Age'].median())


print(df_ecommerce)




df_ecommerce.loc[9,'City']='California'

print(df_ecommerce)


df_ecommerce.loc[21,'City']="Florida"

print(df_ecommerce)




df_ecommerce.loc[12,'Product']='Sofa Come Bed'

print(df_ecommerce)


df_ecommerce.loc[28,'Product']='Textbook'


print(df_ecommerce)



df_ecommerce['Discount_%']=df_ecommerce['Discount_%'].fillna(df_ecommerce['Discount_%'].median())


print(df_ecommerce)


df_ecommerce['Purchase_Date']=df_ecommerce['Purchase_Date'].fillna('2026-05-04')


print(df_ecommerce['Purchase_Date'].dtype)



df_ecommerce['Purchase_Date']=pd.to_datetime(df_ecommerce['Purchase_Date'])

print(df_ecommerce)


print(df_ecommerce['Purchase_Date'].dtype)


print(df_ecommerce)



df_ecommerce=df_ecommerce.sort_values(by='Purchase_Date',ascending=True)

print(df_ecommerce)



df_ecommerce['Age']=df_ecommerce['Age'].astype(int)


df_ecommerce=df_ecommerce.drop_duplicates()


print(df_ecommerce)

# this is bigning :)
# i'm so Happy :) (To BE Best Ai Engineer :)))....)