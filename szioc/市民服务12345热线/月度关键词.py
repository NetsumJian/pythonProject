import numpy as np
import pandas as pd
import os

os.chdir(r'C:\Users\dwx1024047\Documents\Work\12345热线')

data = pd.read_csv('噪音数据源.csv',encoding='gbk')
# df1 = data.groupby(['loc2','work_order_title']).sum(['call_num','call_per'])
# df2 = data.groupby(['loc3','work_order_title']).sum(['call_num','call_per'])
df3 = data.groupby(['loc1','work_order_title']).sum(['call_num','call_per'])
# df1.to_csv('loc2.csv')
# df2.to_csv('loc3.csv')
df3.to_csv('loc1.csv')
# df2 =  data.groupby(['call_month','call_purpose','call_title']).min(['call_rank'])
# del df1['call_rank']
# del df2['call_num']
# del df2['call_person']
# df3 = pd.merge(df1,df2,on=('call_month','call_purpose','call_title'))
# df1.to_csv('bar.csv')