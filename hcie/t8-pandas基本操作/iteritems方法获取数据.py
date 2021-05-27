import pandas as pd
import numpy as np

df4 = pd.DataFrame(np.random.randn(4,3),columns=['c1','c2','c3'])
print('df4: ',df4)
# i = 1
# Data.iteritems 返回一个包含列名称和内容为系列的元组
# for s in df4.iteritems():
#     print('%d列%s'%(i,s))
#     i += 1

# for i in df4['c1']:
#     print(i)
#     print('--'*10)


df4['c1'][2] = 32
print(df4)