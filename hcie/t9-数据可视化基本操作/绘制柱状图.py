import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import mpl

# matplotlib实现
mpl.rcParams['font.sans-serif'] = ['SimHei']
level = ['优秀','不错','666']
x = range(len(level))
y = [1,3,2]
plt.figure(dpi=100)
# bar(
#         x, height, width=0.8, bottom=None, *, align='center',
#         data=None, **kwargs)
plt.bar(x,y,width=0.5,color=['b','r','g'])
plt.xticks(x,level)
plt.grid(linestyle='--',alpha=0.5)
plt.show()

# seaborn 实现
df = pd.DataFrame(['优秀','不错','666','不错','不错','666'],columns=['level'])
# countplot(
#     *,
#     x=None, y=None,
#     hue=None, data=None,
#     order=None, hue_order=None,
#     orient=None, color=None, palette=None, saturation=.75,
#     dodge=True, ax=None, **kwargs
# )
sns.countplot(x='level',data=df)
plt.show()