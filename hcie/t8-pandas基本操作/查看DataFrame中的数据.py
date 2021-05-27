import numpy as np
import pandas as pd

data2 = np.arange(30).reshape(6,5)
df2 = pd.DataFrame(data2,index=['a','b','c','d','e','f'],columns=['A','B','C','D','E'])
print(df2)
print('--'*10)
print(df2.head())
print('--'*10)
print(df2.tail(3))
print('index is :')
print(df2.index)
print('column is :')
print(df2.columns)
print('values is :')
print(df2.values)
print(df2.loc['a':'f':2,'A'])
print(df2.describe())