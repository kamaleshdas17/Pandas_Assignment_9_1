## Using Pandas
#1) How-to-count-distance-to-the-previous-zero

import pandas as pd

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
print('Input DF:\n','-'*10)
print(df)
df1=(df['X']!=0).cumsum()
df2=df1!=df1.shift()
df['Y']=df2.groupby((df2 != df2.shift()).cumsum()).cumsum().astype(int)
print('New DF:\n','-'*20)
print(df)

print('Using Python Code\n','-'*30)
## Using python code	
l=[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]
j=0
for i in l:
    if int(i)>0:
        j+=1
        print(int(i),j)
    elif int(i)==0:
        j=0
        print(int(i),j)
        
        
