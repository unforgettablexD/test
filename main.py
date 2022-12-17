import pandas as pd
import numpy as np
import holidays 
from bdateutil import isbday
from dateutil.parser import ParserError
from statistics import mean
#from pandas.tseries.holiday import India as calendar
df = pd.read_json("Training_Data.json")
df=df[df['Name']=='TERM24975']
df=df.drop(['Name','LastTransaction','Approvals','Denials','Reversals','RespTime','TPS'],axis=1)
df['Date'] = pd.to_datetime(df['StatTime']).dt.date
df['Time'] = pd.to_datetime(df['StatTime']).dt.hour
df["Month"]=pd.to_datetime(df['StatTime']).dt.month_name()
df["Day_of_month"]=pd.to_datetime(df['StatTime']).dt.day
df["weekly_day_index"]=pd.to_datetime(df['StatTime']).dt.weekday
df["Week_label"]=pd.to_datetime(df['StatTime']).dt.day_name()
#df['Holiday'] = df['Date'] in India()
df['Holiday'] =df["StatTime"].apply(lambda x: isbday(x, holidays=holidays.India()))
print(df.head())

#calculating weekdays_hor_average
def weekdays_hour_average(df):
    Week_days=['Monday','Tuesday','Wednesday','Thurday','Friday','Saturday','Sunday']
    #Hours =df['Time'].unique()
    Hours=list(set(df['Time']))
    print(Hours)
    for i in range (0,len(Week_days)):
        df_week=df[df["Week_label"]==Week_days[i]]
        for j in range (0,len(Hours)):
            df_unique_hour=df_week[df_week['Time']==Hours[j]]
            print(df_unique_hour)
            sum_q=df_unique_hour['Total'].mean()
            #sum_t=df_unique_hour.apply(lambda Total:np.mean(Total))
            for k in range (0,len(df['Total'])):
               if (df['Week_label']==Week_days[i] & df['Time']==Hours[j]):
                   df['weekdays_hour_average']=sum_t
    return df

df=weekdays_hour_average(df)
print(df.head())
df.to_csv('file1.csv')

           

