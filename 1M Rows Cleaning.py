import numpy as np
import pandas as pd

df_One_Million=pd.read_csv('used_car_price_prediction_1M.csv')

print(df_One_Million.head(60))


print(df_One_Million.info())




print(df_One_Million['Color'].head(60))



df_One_Million=df_One_Million.drop(columns=['Color','Number_of_Doors','Registration_Age','Tax_Paid'])



print(df_One_Million.info())


print(df_One_Million.head(60))

print(df_One_Million.tail(60))

df_One_Million['Price']=df_One_Million['Price'].astype(int)


print(df_One_Million.head(60))




df_One_Million.loc[df_One_Million['Year']<=2012,'Year']=np.nan

print(df_One_Million['Year'].info())

print(df_One_Million.head(60))


print(df_One_Million.info())



df_One_Million.loc[df_One_Million['Price']==50000,'Price']=np.nan

print(df_One_Million.info())


df_One_Million.loc[df_One_Million['Engine_CC']==800,'Engine_CC']=np.nan

print(df_One_Million.info())


print(df_One_Million.tail(60))


df_One_Million['Year']=df_One_Million['Year'].fillna(df_One_Million.groupby('Model')['Year'].transform('median'))

print(df_One_Million.head(60))



df_One_Million['Price']=df_One_Million['Price'].fillna(df_One_Million.groupby('Model')['Price'].transform('median'))

print(df_One_Million.head(60))



print(df_One_Million.tail(60))


print(df_One_Million.info())



df_One_Million['Price']=df_One_Million['Price'].astype(int)

print(df_One_Million.head(60))




df_One_Million['Mileage_kmpl']=df_One_Million['Mileage_kmpl'].fillna(df_One_Million.groupby('Model')['Mileage_kmpl'].transform('median'))


print(df_One_Million.head(60))


print(df_One_Million.tail(60))



df_One_Million['Mileage_kmpl']=df_One_Million['Mileage_kmpl'].astype(int)


print(df_One_Million.tail(60))


df_One_Million['Year']=df_One_Million['Year'].astype(int)


print(df_One_Million.head(60))


df_One_Million.loc[df_One_Million['Engine_CC']<1000,'Engine_CC']=np.nan

df_One_Million['Engine_CC']=df_One_Million['Engine_CC'].fillna(df_One_Million.groupby('Model')['Engine_CC'].transform('median'))


print(df_One_Million.head(60))

print(df_One_Million.tail(60))

df_One_Million['Engine_CC']=df_One_Million['Engine_CC'].astype(int)


print(df_One_Million.head(60))



df_One_Million.loc[df_One_Million['Horsepower']<=100,'Horsepower']=np.nan



df_One_Million['Horsepower']=df_One_Million['Horsepower'].fillna(df_One_Million.groupby('Engine_CC')['Horsepower'].transform('median'))



print(df_One_Million.head(60))

print(df_One_Million.tail(60))


print(df_One_Million.info())


df_One_Million['Horsepower']=df_One_Million['Horsepower'].astype(float)


df_One_Million['Horsepower']=df_One_Million['Horsepower'].fillna(df_One_Million['Horsepower'].median())


df_One_Million['Horsepower']=df_One_Million['Horsepower'].astype(int)

print(df_One_Million.info())



print(df_One_Million.head(60))


print(df_One_Million.tail(60))



print(df_One_Million['Fuel_Type'].head(60))



df_One_Million.loc[df_One_Million['Fuel_Type']=='Electric','Fuel_Type']=np.nan

print(df_One_Million.info())

print(df_One_Million[['Model','Fuel_Type']].head(60))

print(df_One_Million[['Model','Fuel_Type']].tail(60))


df_One_Million.loc[df_One_Million['Fuel_Type']=='Hybrid','Fuel_Type']=np.nan

print(df_One_Million.info())


df_One_Million.loc[df_One_Million['Model']=='Camry','Fuel_Type']='Hybrid'

print(df_One_Million.info())


print(df_One_Million[['Brand','Model','Fuel_Type']].head(60))

print(df_One_Million[['Brand','Model','Fuel_Type']].tail(60))




df_One_Million.loc[df_One_Million['Brand']=='Mercedes','Fuel_Type']=np.nan

print(df_One_Million[['Brand','Model','Fuel_Type']].tail(60))


df_One_Million.loc[df_One_Million['Brand']=='Audi','Fuel_Type']=np.nan

df_One_Million.loc[df_One_Million['Brand']=='BMW','Fuel_Type']=np.nan

df_One_Million.loc[df_One_Million['Brand']=='Ford','Fuel_Type']=np.nan

print(df_One_Million.info())

print(df_One_Million[['Brand','Model','Fuel_Type']].tail(60))

df_One_Million.loc[df_One_Million['Brand']=='Mercedes','Fuel_Type']='Diesel'

print(df_One_Million[['Brand','Model','Fuel_Type']].tail(60))


df_One_Million.loc[df_One_Million['Brand']=='BMW','Fuel_Type']='Diesel'


df_One_Million.loc[df_One_Million['Brand']=='Audi','Fuel_Type']='Petrol'


df_One_Million.loc[df_One_Million['Brand']=='Ford','Fuel_Type']='Diesel'



df_One_Million.loc[df_One_Million['Brand']=='Mahindra','Fuel_Type']=np.nan

df_One_Million.loc[df_One_Million['Brand']=='Toyota','Fuel_Type']=np.nan


print(df_One_Million.info())



df_One_Million.loc[df_One_Million['Brand']=='Mahindra','Fuel_Type']='Diesel'

df_One_Million.loc[df_One_Million['Brand']=='Toyota','Fuel_Type']='Diesel'

print(df_One_Million.info())

print(df_One_Million[['Brand','Model','Fuel_Type']].tail(60))



df_One_Million.loc[df_One_Million['Brand']=='Volkswagen','Fuel_Type']=np.nan

print(df_One_Million[['Brand','Model','Fuel_Type']].tail(60))

df_One_Million.loc[df_One_Million['Brand']=='Volkswagen','Fuel_Type']='Petrol'



df_One_Million['Fuel_Type']=df_One_Million['Fuel_Type'].fillna('Petrol')


print(df_One_Million.info())

print(df_One_Million[['Brand','Model','Fuel_Type']].tail(60))

print(df_One_Million[['Brand','Model','Fuel_Type']].head(60))





print(df_One_Million['Transmission'].head(60))

print(df_One_Million[['Brand','Model','Transmission']].head(60))

print(df_One_Million[['Brand','Model','Transmission']].tail(60))



df_One_Million['Transmission']=df_One_Million['Transmission'].fillna('Automatic')

print(df_One_Million['Transmission'].head(60))

print(df_One_Million.info())



print(df_One_Million['City'].head(60))


print(df_One_Million['City'].tail(60))

print(df_One_Million[['City','Brand','Model','Price']].tail(60))

print(df_One_Million[['City','Brand','Model','Price']].head(60))


df_One_Million['City']=df_One_Million['City'].fillna('Ahemdabad')


print(df_One_Million[['City','Brand','Model','Price']].head(60))

print(df_One_Million[['City','Brand','Model','Price']].tail(60))



print(df_One_Million.info())



df_One_Million=df_One_Million.drop_duplicates()

print(df_One_Million.info())

df_One_Million.to_csv('1M rows Dataset Cleaning.csv',index=False)




