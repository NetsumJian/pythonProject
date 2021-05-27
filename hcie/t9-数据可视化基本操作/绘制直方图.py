import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

t = np.random.randint(0,30,90)
print(t)
plt.figure(dpi=100)
distance = 2
group_num = int((max(t)-min(t))/distance)
# hist(
#         x, bins=None, range=None, density=False, weights=None,
#         cumulative=False, bottom=None, histtype='bar', align='mid',
#         orientation='vertical', rwidth=None, log=False, color=None,
#         label=None, stacked=False, *, data=None, **kwargs)
# 绘制直方图
plt.hist(t,facecolor='blue',edgecolor='black',alpha=0.7)
plt.xticks(range(min(t),max(t))[::2])
plt.grid(linestyle='-.',alpha=0.5)
plt.show()

# seaborn 实现直方图
sns.histplot(t,kde=True)
plt.show()