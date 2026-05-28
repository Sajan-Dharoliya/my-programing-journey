import numpy as np
import pandas as pd

# Global E-Commerce Mega Dataset - Version 7 (Pro Challenge)
pro_international_data = {
    "Customer_ID": [801, 802, 803, 804, 805, 806, 807, 801, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819,
                    820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839,
                    840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859],
    
    "Customer_Name": ["John Miller", "Olivia Garcia", "Ethan Martinez", "Sophia Robinson", "Liam Clark", "Ava Rodriguez", "Noah Lewis", "John Miller", "Isabella Lee", "Lucas Walker",
                     "Mia Hall", "Mason Allen", "Amelia Young", "Logan King", "Harper Wright", "Ethan Martinez", "Evelyn Scott", "Oliver Torres", "Charlotte Nguyen", "Elijah Hill",
                     "Amelia Young", "James Adams", "Emily Baker", "Benjamin Green", "Abigail Adams", "Alexander Nelson", "Emily Baker", "Jacob Carter", "Elizabeth Mitchell", "Michael Perez",
                     "Sofia Roberts", "William Turner", "Avery Phillips", "James Adams", "Ella Campbell", "Daniel Parker", "Madison Evans", "Matthew Edwards", "Scarlett Collins", "Henry Stewart",
                     "Chloe Morris", "Jackson Nguyen", "Camila Rogers", "Sebastian Reed", "Aria Cook", "Jack Morgan", "Grace Bell", "Owen Murphy", "Chloe Morris", "Aiden Bailey",
                     "Lily Rivera", "Matthew Edwards", "Zoey Cooper", "Samuel Richardson", "Penelope Cox", "David Howard", "Riley Ward", "Joseph Torres", "Zoey Cooper", "Samuel Peterson"],
    
    "Age": [31.0, np.nan, 25.0, 42.0, -15.0, 58.0, 150.0, 31.0, 22.0, np.nan, 29.0, 47.0, 115.0, 20.0, 33.0, 25.0, 50.0, -5.0, 37.0, 40.0,
            115.0, 35.0, 27.0, np.nan, 48.0, 18.0, 27.0, 31.0, 60.0, 24.0, 52.0, 29.0, -8.0, 35.0, 43.0, 130.0, 26.0, 39.0, np.nan, 46.0,
            34.0, 23.0, 55.0, 30.0, 142.0, -12.0, 38.0, 41.0, 34.0, 28.0, np.nan, 39.0, 32.0, 45.0, 21.0, 51.0, -2.0, 36.0, 32.0, 49.0],
    
    "City": ["New York", "London", "Los Angeles", "New York", "Miami", "Paris", "Tokyo", "New York", "Sydney", np.nan, "Chicago", "Toronto", "New York", "London", "Los Angeles", "Los Angeles", "Miami", "Paris", "Tokyo", "Sydney",
             "New York", "Chicago", "Toronto", "London", "Miami", "Paris", "Toronto", "Tokyo", "Sydney", "Chicago", "New York", "London", "Los Angeles", "Chicago", "Miami", "Paris", "Tokyo", "Sydney", "Chicago", "Toronto",
             "New York", np.nan, "Los Angeles", "London", "Miami", "Paris", "Toronto", "Tokyo", "New York", "Chicago", "London", "Sydney", "Miami", "Paris", "Toronto", "Tokyo", "Sydney", "Chicago", "Miami", "London"],
    
    "Subscription_Tier": ["Bronze", "Silver", "Gold", "Bronze", "Silver", "Gold", "Bronze", "Bronze", "Silver", "Gold", "Bronze", "Silver", "Gold", "Bronze", "Silver", "Gold", "Bronze", "Silver", "Gold", "Bronze",
                          "Gold", "Silver", "Platinum", "Silver", "Gold", "Bronze", "Platinum", "Gold", "Bronze", "Silver", "Platinum", "Silver", "Gold", "Silver", "Bronze", "Gold", "Platinum", "Bronze", "Silver", "Gold",
                          "Bronze", "Silver", "Gold", "Bronze", "Silver", "Gold", "Platinum", "Bronze", "Bronze", "Silver", "Gold", "Bronze", "Silver", "Gold", "Platinum", "Bronze", "Silver", "Gold", "Silver", "Gold"],
    
    "Payment_Method": ["Credit Card", "PayPal", "Crypto", "Credit Card", "PayPal", "Crypto", "Credit Card", "Credit Card", "PayPal", "Crypto", np.nan, "Bank Transfer", "Credit Card", "PayPal", "Crypto", "Crypto", "PayPal", np.nan, "Credit Card", "PayPal",
                      "Credit Card", "Bank Transfer", "PayPal", "Crypto", "Credit Card", "PayPal", "PayPal", "Crypto", "Bank Transfer", "Credit Card", "PayPal", "Crypto", "Bank Transfer", "Bank Transfer", "Credit Card", "PayPal", "Crypto", "Bank Transfer", np.nan, "Credit Card",
                      "PayPal", "Crypto", "Bank Transfer", "Credit Card", "PayPal", "Crypto", "Bank Transfer", "Credit Card", "PayPal", "Crypto", "Bank Transfer", "Credit Card", "PayPal", "Crypto", "Bank Transfer", "Credit Card", "PayPal", "Crypto", "PayPal", "Bank Transfer"],
    
    "Product": ["Laptop", "Smartphone", "Watch", "Laptop", "Earphones", "Tablet", "Laptop", "Laptop", "Smartwatch", "Trimmer", np.nan, "Speakers", "Router", "Watch", "Earphones", "Watch", "Smartphone", "Tablet", np.nan, "Laptop",
                "Router", "Smartwatch", "Trimmer", "Speakers", "Router", "Watch", "Trimmer", "Earphones", "Smartphone", "Tablet", "Laptop", "Smartwatch", "Trimmer", "Smartwatch", "Speakers", "Router", "Watch", "Earphones", "Smartphone", "Tablet",
                "Laptop", "Smartwatch", "Trimmer", "Speakers", "Router", "Watch", "Earphones", "Smartphone", "Tablet", "Laptop", "Smartwatch", "Trimmer", "Speakers", "Router", "Watch", "Earphones", "Smartphone", "Tablet", "Speakers", "Router"],
    
    "Price": [1200, 800, 350, 1200, 45, "150", 1100, 1200, 250, 40, 600, 95, 55, 320, 35, 350, "850", 180, 120, 1050,
              55, 220, 38, 110, 60, 340, 38, 50, 799, 190, 1200, 220, 38, 220, 95, 55, 340, 50, 799, 190,
              1200, 220, 38, 95, 55, 340, 50, 799, 190, 1050, 40, 799, 95, 55, 340, 50, 799, 190, 95, 55],
    
    "Purchase_Date": ["2026-05-01", "2026-05-02", "2026-05-03", "2026-05-01", "2026-05-05", np.nan, "2026-05-07", "2026-05-01", "2026-05-09", "2026-05-10", 
                     "2026-05-11", "2026-05-12", "2026-05-13", "2026-05-14", "2026-05-15", "2026-05-03", "2026-05-17", "2026-05-18", "2026-05-19", "2026-05-20",
                     "2026-05-13", "2026-05-22", "2026-05-23", "2026-05-24", "2026-05-25", "2026-05-26", "2026-05-23", "2026-05-28", "2026-05-29", "2026-05-30",
                     "2026-05-01", "2026-05-02", "2026-05-03", "2026-05-22", "2026-05-05", "2026-05-06", "2026-05-07", "2026-05-08", "2026-05-09", "2026-05-10",
                     "2026-05-11", "2026-05-12", "2026-05-13", "2026-05-14", "2026-05-15", "2026-05-16", "2026-05-17", "2026-05-18", "2026-05-11", "2026-05-20",
                     "2026-05-21", "2026-05-08", "2026-05-23", "2026-05-24", "2026-05-25", "2026-05-26", "2026-05-27", "2026-05-28", "2026-05-23", "2026-05-30"]
}

df_pro = pd.DataFrame(pro_international_data)
print("--- 🚨 Hardcore Pro Dataset Loaded (60 Rows)! ---")
print(df_pro.head())




print(df_pro)

print(df_pro.info())



print(df_pro.describe())

print(df_pro['Price'].dtype)


df_pro['Price']=df_pro['Price'].astype(int)


print(df_pro.describe())


print(df_pro)



df_pro.loc[4,'Age']=15

print(df_pro)


df_pro.loc[17,'Age']=18

print(df_pro)



df_pro.loc[df_pro['Age']<0,'Age']=np.nan

print(df_pro)



df_pro.loc[df_pro["Age"]>100,'Age']=np.nan

print(df_pro)


print(df_pro.info())

df_pro['Age']=df_pro['Age'].fillna(df_pro['Age'].median())

print(df_pro)


df_pro['Age']=df_pro['Age'].astype(int)

print(df_pro)


df_pro.loc[9,'City']='California'

print(df_pro)




df_pro.loc[41,'City']='Florida'



print(df_pro)


print(df_pro.isnull().sum())



print(df_pro)





subscription_rule={'Bronze':0,'Silver':1,'Gold':2,'Platinum':3}


df_pro['Subscription_Tier']=df_pro['Subscription_Tier'].map(subscription_rule)


print(df_pro)




df_pro.loc[10,'Payment_Method']='PayPal'


print(df_pro)



df_pro.loc[17,'Payment_Method']='Credit Card'

print(df_pro)



df_pro.loc[38,'Payment_Method']='PayPal'

print(df_pro)





print(df_pro.isnull().sum())


print(df_pro)



df_pro.loc[10,'Product']='Monitor'


print(df_pro)


df_pro.loc[18,'Product']='Earphones'


print(df_pro)



df_pro['Purchase_Date']=df_pro['Purchase_Date'].fillna('2026-05-04')

print(df_pro)


df_pro=pd.get_dummies(df_pro,columns=['Payment_Method'],dtype=int)


print(df_pro.columns)


print(df_pro.info())



df_pro['Purchase_Date']=df_pro['Purchase_Date']=pd.to_datetime(df_pro['Purchase_Date'])

print(df_pro)


df_pro=df_pro.sort_values(by='Purchase_Date',ascending=True)


df_pro=df_pro.drop_duplicates()

df_pro.to_csv('Dateset 6 cleaning.csv',index=False)


# i'm so happy
# this is bigning :) (To Best Ai Engineer :)...)