import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-whitegrid')
x = np.arange(0,3*np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# subplot(nrows, ncols, index, **kwargs)
plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title('sin')
plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('cos')
plt.show()