import pandas as pd
import os

os.chdir(r'C:\Users\dwx1024047\Documents\Work\12345热线\V3')
data = pd.read_excel('rfm.xlsx',index_col='来电标题')
data.head()
r=list(data['R'])
f=list(data['F'])
m=list(data['M'])

from pandas import DataFrame

cdata = DataFrame([r,f,m]).T
cdata.head()

cdata.index = data.index
cdata.columns = ['R','F','M']
cdata.head()

from sklearn.cluster import KMeans

kmodel = KMeans(n_clusters=8,n_jobs=4,max_iter=100,random_state=0)
kmodel.fit(cdata)

from pandas import Series

Series(kmodel.labels_).value_counts()

res = pd.concat([cdata,Series(kmodel.labels_,index=cdata.index)],axis = 1)
res.head()

res.columns=list(cdata.columns)+['类别']

ts = res.groupby('类别').mean()

ts.to_excel('ts.xlsx')

res.to_excel('res.xlsx')