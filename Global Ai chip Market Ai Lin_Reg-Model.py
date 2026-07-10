import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score


df_chip_blobal=pd.read_csv('ai_chip_market.csv')



print(df_chip_blobal.head(10))


print(df_chip_blobal.info())


print(df_chip_blobal[['year','chip_name','vendor','launch_date','memory_gb']].head(60))

print(df_chip_blobal[['year','chip_name','vendor','launch_date','memory_gb']].tail(60))


print(df_chip_blobal[['fp16_tflops','tdp_watts','estimated_shipments_units','estimated_asp_usd','estimated_revenue_usd_m','description']].head(60))


print(df_chip_blobal[['fp16_tflops','tdp_watts','estimated_shipments_units','estimated_asp_usd','estimated_revenue_usd_m','description']].tail(60))


df_chip_blobal.loc[df_chip_blobal['memory_gb']==0,'memory_gb']=np.nan

df_chip_blobal['memory_gb']=df_chip_blobal['memory_gb'].fillna(44)

print(df_chip_blobal['memory_gb'].tail(60))


df_chip_blobal['memory_gb']=df_chip_blobal['memory_gb'].astype(int)

print(df_chip_blobal.tail(60))



print(df_chip_blobal.tail(60))



df_chip_blobal.loc[df_chip_blobal['chip_name']=='NVIDIA B300','estimated_shipments_units']=5000000



df_chip_blobal.loc[df_chip_blobal['chip_name']=='NVIDIA B300','estimated_revenue_usd_m']=50000


df_chip_blobal.loc[df_chip_blobal['chip_name']=='AMD MI300X','estimated_shipments_units']=27000

df_chip_blobal.loc[df_chip_blobal['chip_name']=='AMD MI300X','estimated_revenue_usd_m']=400



print(df_chip_blobal[['estimated_shipments_units','estimated_revenue_usd_m']].head(60))

print(df_chip_blobal[['year','chip_name','estimated_shipments_units','estimated_asp_usd','estimated_revenue_usd_m']].tail(60))



df_chip_blobal.loc[65,'estimated_shipments_units']=49000





df_chip_blobal.loc[65,'estimated_asp_usd']=15000

df_chip_blobal.loc[65,'estimated_revenue_usd_m']=750


df_chip_blobal.loc[66,'estimated_shipments_units']=300000

df_chip_blobal.loc[66,'estimated_asp_usd']=14000

df_chip_blobal.loc[66,'estimated_revenue_usd_m']=4200


df_chip_blobal.loc[67,'estimated_shipments_units']=500000

df_chip_blobal.loc[67,'estimated_asp_usd']=12000

df_chip_blobal.loc[67,'estimated_revenue_usd_m']=6000


df_chip_blobal.loc[68,'estimated_shipments_units']=500000

df_chip_blobal.loc[68,'estimated_asp_usd']=10000

df_chip_blobal.loc[68,'estimated_revenue_usd_m']=5000

print(df_chip_blobal[['year','chip_name','estimated_shipments_units','estimated_asp_usd','estimated_revenue_usd_m']].tail(60))



df_chip_blobal.loc[69,'estimated_shipments_usd']=100000

df_chip_blobal.loc[69,'estimated_asp_usd']=18000

df_chip_blobal.loc[69,'estimated_revenue_usd_m']=1800


df_chip_blobal.loc[70,'estimated_shipments_usd']=600000

df_chip_blobal.loc[70,'estimated_asp_usd']=16500

df_chip_blobal.loc[70,'estimated_revenue_usd_m']=9900


df_chip_blobal.loc[71,'estimated_shipments_units']=1600000

df_chip_blobal.loc[71,'estimated_asp_usd']=15000

df_chip_blobal.loc[71,'estimated_revenue_usd_m']=24000



df_chip_blobal.loc[72,'estimated_shipments_units']=10000

df_chip_blobal.loc[72,'estimated_asp_usd']=25000

df_chip_blobal.loc[72,'estimated_revenue_usd_m']=250



df_chip_blobal.loc[74,'estimated_shipments_units']=40000

df_chip_blobal.loc[74,'estimated_asp_usd']=15000

df_chip_blobal.loc[74,'estimated_revenue_usd_m']=3300


df_chip_blobal.loc[77,'estimated_shipments_units']=15000

df_chip_blobal.loc[77,'estimated_asp_usd']=6000

df_chip_blobal.loc[77,'estimated_revenue_usd_m']=90



print(df_chip_blobal[['year','chip_name','estimated_shipments_units','estimated_asp_usd','estimated_revenue_usd_m']].tail(60))


print(df_chip_blobal.info())

df_chip_blobal=df_chip_blobal.drop(columns=['description','estimated_shipments_usd'])

print(df_chip_blobal.info())


df_chip_blobal['launch_date']=pd.to_datetime(df_chip_blobal['launch_date'])

df_chip_blobal['launch_date'].dt.year

df_chip_blobal['launch_date']=pd.to_numeric(df_chip_blobal['launch_date'],downcast='integer')
# line 157\159 ^^^^^^^^^^^^^^ i do this after by hitting by an error :)


df_chip_blobal['estimated_shipments_units']=pd.to_numeric(df_chip_blobal['estimated_shipments_units'],downcast='integer')


print(df_chip_blobal.info())

df_chip_blobal['year']=pd.to_numeric(df_chip_blobal['year'],downcast='integer')

df_chip_blobal['memory_gb']=pd.to_numeric(df_chip_blobal['memory_gb'],downcast='integer')

df_chip_blobal['fp16_tflops']=pd.to_numeric(df_chip_blobal['fp16_tflops'],downcast='integer')

df_chip_blobal['tdp_watts']=pd.to_numeric(df_chip_blobal['tdp_watts'],downcast='integer')

df_chip_blobal['estimated_asp_usd']=pd.to_numeric(df_chip_blobal['estimated_asp_usd'],downcast='integer')


df_chip_blobal['estimated_revenue_usd_m']=df_chip_blobal['estimated_revenue_usd_m'].astype(int)


print(df_chip_blobal.info())


df_chip_blobal['estimated_revenue_usd_m']=pd.to_numeric(df_chip_blobal['estimated_revenue_usd_m'],downcast='integer')




df_chip_blobal=pd.get_dummies(df_chip_blobal,columns=['chip_name','vendor'],dtype='int8')

print(df_chip_blobal.info())



y=df_chip_blobal['estimated_revenue_usd_m']

X=df_chip_blobal.drop(columns=['estimated_revenue_usd_m'])

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)



Model=LinearRegression()

Model.fit(X_train,y_train)

Predictions=Model.predict(X_test)


Comperison_Table=pd.DataFrame({'Real Revenue':y_test,'Ai Predictions':Predictions.astype(int)})



mae=mean_absolute_error(y_test,Predictions)


r2=r2_score(y_test,Predictions)

print(f'Mean Absolute Error (MAE): ${mae:.2f}')

print(f'Model Accuracy Score (R2 Score):{r2*100:.2f}%')

# Mean Absolute Error (MAE):
# $3422.80


# Model Accuracy Score (R2):
# (R2 Score): 59.06%

# so that's it and be postive guys :)