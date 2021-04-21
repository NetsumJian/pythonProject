import numpy as np
from scipy.linalg import eig
import matplotlib.pyplot as plt

A = [[1,2],[2,1]]
evals,evecs=eig(A)
evecs=evecs[:,0],evecs[:,1]
fig,ax=plt.subplots()

for spine in ['left','bottom']:
    ax.spines[spine].set_position('zero')

ax.grid(alpha=0.4)
xmin,xmax=-3,3
ymin,ymax=-3,3
ax.set(xlim=(xmin,xmax),ylim=(ymin,ymax))

for v in evecs:
    ax.annotate(text="",xy=v,xytext=(0,0),
                arrowprops=dict(facecolor='blue',
                                shrink=0,
                                alpha=0.6,
                                width=0.5))

x=np.linspace(xmin,xmax,3)
for v in evecs:
    a=v[1]/v[0]
    ax.plot(x,a*x,'r-',lw=0.4)

plt.show()
