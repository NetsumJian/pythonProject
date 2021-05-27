import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# matplotlib 实现

a = np.random.randint(0,20,15)
b = np.random.randint(0,20,15)
s = np.random.randint(0,100,15)
print(a)
print(b)
# scatter(
#         x, y, s=None, c=None, marker=None, cmap=None, norm=None,
#         vmin=None, vmax=None, alpha=None, linewidths=None,
#         verts=cbook.deprecation._deprecated_parameter,
#         edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)
# x,y 表示xy轴的数据,s 表示标量,c表示颜色,marker表示标记样式
plt.scatter(a,b,s)
plt.show()

# seaborn实现
df = pd.DataFrame({'x':a,'y':b})
# jointplot(
#     *,
#     x=None, y=None,
#     data=None,
#     kind="scatter", color=None, height=6, ratio=5, space=.2,
#     dropna=False, xlim=None, ylim=None, marginal_ticks=False,
#     joint_kws=None, marginal_kws=None,
#     hue=None, palette=None, hue_order=None, hue_norm=None,
#     **kwargs
# )
sns.jointplot(x='x',y='y',data=df)
plt.show()