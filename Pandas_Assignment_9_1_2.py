import pandas as pd
import numpy as np

#Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers.
print('Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers\n','-'*100)
indexdata=pd.date_range('2015-01-01','2015-12-31',freq='B')
df=pd.DataFrame({'Value':np.random.randint(1,100,len(indexdata)).tolist()},index=indexdata)

print('\nTop 5 records from DataFrame\n','-'*30)

print(df.head())


#Find the sum of the values in s for every Wednesday
#wed=pd.date_range('2015-01-01','2015-12-31',freq='B')
#print('Sum of value of wednesday: ',df1.loc[wed[wed.weekday==2].tolist()].sum())
print('\nSum of value of wednesday: ',df[df.index.weekday==2].sum())


print('\nAverage For each calendar month\n','-'*30)
#Average For each calendar month
print(df.resample('M').mean())

#For each group of four consecutive calendar months in s, find the date on which the highest value occurred.
print('\nFor each group of four consecutive calendar months, find the date on which the highest value occurred \n','-'*100)
df1=df.groupby(pd.Grouper(freq='4M'))
print(df1.idxmax())

print('\nFor validation, printing groups with value:\n','-'*50)
for name,grp in df1:
	print('Group name: ',name)
	print(grp.to_string())
