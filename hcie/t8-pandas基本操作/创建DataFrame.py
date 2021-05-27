import pandas as pd
import numpy as np

# pd.date_range(
#     start=None, 指定日期起点
#     end=None, 指定日期终点
#     periods=None, 指定个数
#     freq=None, 代表间隔
#     tz=None, 指定时区
#     normalize=False,
#     name=None,
#     closed=None,
#     **kwargs,
# ) -> DatetimeIndex
# 生成一个时间序列的索引 DatetimeIndex
ds = pd.date_range('20190101', periods=7)
print(ds)
print('--'*16)

# pd.DataFrame(
#         data=None,
#         index: Optional[Axes] = None,
#         columns: Optional[Axes] = None,
#         dtype: Optional[Dtype] = None,
#         copy: bool = False,
#     )
# 生成一个DataFrame数据,data是数据,index是索引,columns是列名
df = pd.DataFrame(np.random.randn(7,4),index=ds,columns=list('abcd'))
print(df)

df1 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20190102'), #生成时间戳
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    # Categoricals 是pandas的一种数据类型,对应着被统计的变量
                    # Categorical 类型的数据可以具有特定的顺序,这个顺序是创建时手工设定的,是静态的
                    'E':pd.Categorical(['test','train','test','train']),
                    'F':'foo'})
print(df1)