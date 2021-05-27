import numpy as np
import pandas as pd

data2 = np.arange(30).reshape(6,5)
df2 = pd.DataFrame(data2,index=['a','b','c','d','e','f'],columns=['A','B','C','D','E'])

# drop(
#         labels=None, 标签名
#         axis=0, 选择行或列 ( 0 表示行, 1 表示列)
#         index=None, 直接指定要删除的行
#         columns=None, 直接指定要删除的列
#         level=None,
#         inplace=False, 默认该删除操作不改变原数据,而是返回一个执行删除操作后的新 DataFrame
#         errors="raise",
#     )
# 通过指定标签名称和相应的轴,或直接指定索引列或名称来删除行或列
a = df2.drop(['a'],axis=0)
b = df2.drop(['A'],axis=1)
print('-----原始数据-----')
print(df2)
print('---行---')
print(a)
print('---列---')
print(b)

# append(
#         other, ignore_index=False, verify_integrity=False, sort=False
#     ) -> "DataFrame"
# 将其他行附加到调用这的末尾,返回一个新对象.other 为要追加的数据
c = b.append(a)
print(b)
print('---合并数据---')
print(c)

# reset_index(
#         默认为 none 仅从索引中删除给定的级别,默认情况下删除所有级别
#         level: Optional[Union[Hashable, Sequence[Hashable]]] = None,
#         drop: bool = False, 表示是否将索引添加至数据成为一列
#         inplace: bool = False, 为 True 时会修改原数据, 为 False 会产生新的数据
#         col_level: Hashable = 0,
#         col_fill: Label = "",
#     ) -> Optional["DataFrame"]
# 重置索引
b.reset_index(inplace=True)
print(b)