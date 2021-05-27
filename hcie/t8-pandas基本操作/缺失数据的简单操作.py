import numpy as np
import pandas as pd

df6 = pd.DataFrame(np.random.randn(5,3),index=list('acefh'),columns=['one','two','three'])
print(df6)
df6 = df6.reindex(list('abcdefgh'))
print(df6)
print(df6['one'].isnull())
print(df6['one'].sum())
df7 = pd.DataFrame(np.random.randn(3,3),index=list('ace'),columns=['one','two','three'])
df7 = df7.reindex(['a','b','c'])
print(df7)
print('NaN replaced with "0" :')

# fillna(
#         value=None, 填充数据
#         method=None, 表示填充方法 (backfill,bfill,pad,ffill,None)
#         axis=None,
#         inplace=False,
#         limit=None,
#         downcast=None,
#     ) -> Optional["DataFrame"]
# 使用指定的方法和数据填充 NA/NaN值
print(df7.fillna(0))
print(df6)

# dropna(self, axis=0, how="any", thresh=None, subset=None, inplace=False)
# 删除缺失值,how 表示删除的方式 (any:删除存在 NA 值的行或列; all:删除全部为 NA 的行或列)
print('--'*10)
df6['one']['g'] = 20
print(df6['one'])
print(df6.dropna(how='all'))