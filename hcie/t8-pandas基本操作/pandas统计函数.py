import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4,5,4])

# pct_change(
#         periods=1, 为形成百分比变化的时期
#         fill_method="pad", 为如何在计算百分比变化之前处理 NA
#         limit=None, 表示停止前要填充的连续 NA 的数量
#         freq=None,
#         **kwargs,
#     ) -> FrameOrSeries
# 当前元素和先前元素之间的百分比变化
print(s.pct_change())
df5 = pd.DataFrame(np.random.randn(5,2))
print(df5)
print(df5.pct_change())

s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print('s1: ',s1)
print('s2: ',s2)

# cov(
#         other: "Series",
#         min_periods: Optional[int] = None, 表示每个列对所需的最小观测值数
#         ddof: Optional[int] = 1,
#     ) -> float
# 计算列的协方差,不包括 NA/null 值
print('协方差: ',s1.cov(s2))

frame = pd.DataFrame(np.random.randn(10,5),columns=['a','b','c','d','e'])
print(frame['a'].cov(frame['b']))
print(frame.cov())

s3 = pd.Series(np.random.randn(5),index=list('abcde'))
print(s3)
s3['d'] = s3['b']

# rank(
#         axis=0, 选择行或列
#         method: str = "average", 表示对平均值排名,(average,min,max,first,dense)
#         numeric_only: Optional[bool_t] = None,
#         na_option: str = "keep", 表示将 NA 值保留在原来的位置
#         ascending: bool_t = True, 表示降序排序
#         pct: bool_t = False,
#     ) -> FrameOrSeries
# 返回数据的排名
print(s3.rank())