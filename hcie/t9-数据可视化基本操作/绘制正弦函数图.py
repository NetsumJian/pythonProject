import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 选择图形主题
# 暗网格-darkgrid,白网格-whitegrid,全黑-dark,全白-white,全刻度-ticks
plt.style.use('seaborn-darkgrid')
x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()

