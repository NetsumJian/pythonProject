import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-dark')
plt.figure(figsize=(8,6),dpi=80)
plt.subplot(111)
x = np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s=np.cos(x),np.sin(x)
#plt.plot(x,c,color='blue',linewidth=1.0,label='blue',linestyle='--')
plt.plot(x,c,color='blue',linewidth=3.0,label='blue',linestyle='dashed')
#plt.plot(x,s,color='green',linewidth=1.0,label='green',linestyle='--')
plt.plot(x,s,color='green',linewidth=2.0,label='green',linestyle='-.')
plt.legend()
plt.xlim(-4.0,4.0)
plt.xticks(np.linspace(-4,4,9,endpoint=True))
plt.ylim(-1.0,1.0)
plt.yticks(np.linspace(-1,1,5,endpoint=True))
plt.savefig('exercice.png',dpi=72)
plt.show()
