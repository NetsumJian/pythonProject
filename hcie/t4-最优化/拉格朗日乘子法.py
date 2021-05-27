from scipy.optimize import minimize
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

# 定义目标函数 (a-b*x[0])**2 + (c-d*x[1])**2
def func(a,b,c,d):
    fun = lambda x:(a-b*x[0])**2 + (c-d*x[1])**2
    return fun

# 约束条件,包括等式约束和不等式约束
def con(args):
    # type 定义约束为等式还是不等式 ; fun 约束函数
    cons = ({'type':'ineq','fun':lambda x:abs(x[0])+abs(x[1])-args})
    return cons

# 画三维模式图
def draw3D():
    # 新建绘图
    fig = plt.figure()
    # 添加三维坐标轴
    ax = Axes3D(fig)
    # 定义 x,y 坐标的范围;meshgrid 函数用两个坐标轴上的点在平面上画格
    x_arange=np.arange(-10,10)
    y_arange=np.arange(-10,10)
    X,Y = np.meshgrid(x_arange,y_arange)
    # Z1 为目标函数; Z2 为约束条件
    Z1 = (2-X) ** 2 + (3-2*Y) **2
    Z2 = abs(X)+abs(Y)-4
    # 作图
    plt.xlabel('x')
    plt.ylabel('y')
    # 做三维曲面图,rstride 和 cstride 分别代表行和列的跨度; cmap 曲面颜色
    ax.plot_surface(X,Y,Z1,rstride=1,cstride=1,cmap='rainbow')
    ax.plot_surface(X,Y,Z2,rstride=1,cstride=1,cmap='rainbow')
    plt.show()

# 画等高线图
def drawContour():
    x_arange = np.linspace(-10.0,10.0,256)
    y_arange = np.linspace(-10.0,10.0,256)
    X,Y = np.meshgrid(x_arange,y_arange)
    Z1 = (2 - X) ** 2 + (3 - 2 * Y) ** 2
    Z2 = abs(X) + abs(Y) - 4
    plt.xlabel('x')
    plt.ylabel('y')
    # 做目标函数和约束条件的等高线, 8代表等高线的密集度; alpha 等高线透明度; cmap 颜色
    # contourf 对等高线间的填充区域进行填充; contour 画等高线
    plt.contourf(X,Y,Z1,8,alpha=0.75,cmap='rainbow')
    plt.contourf(X,Y,Z2,8,alpha=0.75,cmap='rainbow')
    C1 = plt.contour(X,Y,Z1,16,colors='black')
    C2 = plt.contour(X,Y,Z2,8,colors='black')
    # 为等高线加上 label, inline 为真, label 写在等高线里; fontsize 字体大小
    plt.clabel(C1,inline=True,fontsize=10)
    plt.clabel(C2,inline=True,fontsize=10)
    plt.show()

if __name__ == '__main__':
    # 约束条件 |x0| + |x1| = 4
    cons = con(4)
    # 初始值的设置很重要,很容易收敛到另外极值点,需多试几个值
    '''
    求解目标函数最小值, func 是个残差函数; x0 是计算的初始参数值;
    把残差函数中除了初始化以外的参数打包到 args 中;
    method 优化方法, 包括'BFGS','SLSQP','Newton-CG';
    constraints 为约束条件
    '''
    x0 = np.array((1,1))
    res = minimize(func(2,1,3,2),x0,method='SLSQP',constraints=cons)
    # 输出函数值
    print('min fun = ',res.fun)
    # 输出最优化是否成功
    print('success ?:',res.success)
    # 输出最优点
    print('optimum point:',res.x)
    # 调用函数作图
    draw3D()
    drawContour()