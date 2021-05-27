import pandas as pd
import numpy as np

# pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
# 生成一个Series数据.data为数据可以是数组和字典等,index为索引值,要求与数据长度相同,dtype为数据类型
s = pd.Series([1,3,5,np.nan,6,9])
print(s)

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

'''
字典 (dict) 可以作为输入传递,如果没有指定索引,则按排序顺序取得字典键以构造索引.
如果传递了索引,索引中与标签对应的数据中的值将被取出
'''
d1 = {'a':0,'b':1,'c':2}
s = pd.Series(d1,index=['a','c'])
print(s)