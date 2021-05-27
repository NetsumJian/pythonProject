import numpy as np
import scipy as sp
import pylab as pl
from scipy.optimize import leastsq

n = 9

# 定义目标函数
def real_func(x):
    return np.sin(2*np.pi*x)

# 定义拟合函数
def fit_func(p,x):
    f = np.poly1d(p)
    return f(x)

# 定义残差函数
def residuals_func(p,y,x):
    ret = fit_func(p,x)-y
    return ret

# 随机选择 9 个点作为 x
x=np.linspace(0,1,9)

x_points=np.linspace(0,1,1000)
y0=real_func(x)
y1=[np.random.normal(0,0.1)+y for y in y0]
p_init=np.random.randn(n)
plsq=leastsq(func=residuals_func,x0=p_init,args=(y1,x))
print('Fitting Parameters: ',plsq[0])
pl.plot(x_points,real_func(x_points),label='real')
pl.plot(x_points,fit_func(plsq[0],x_points),label='fitted curve')
pl.plot(x,y1,'bo',label='with noise')
pl.legend()
pl.show()