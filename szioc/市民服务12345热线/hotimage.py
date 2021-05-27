import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import os

# 画三维模式图
def draw3D(x,y,z):
    # 新建绘图
    fig = plt.figure()
    # 添加三维坐标轴
    ax = Axes3D(fig)
    # 定义 x,y 坐标的范围;meshgrid 函数用两个坐标轴上的点在平面上画格
    x_arange=np.arange(22.5,23.5,0.05)
    y_arange=np.arange(113,115,0.05)
    # 作图
    # ax.fmt_zdata(z)
    plt.xlabel('x')
    plt.ylabel('y')
    # 做三维曲面图,rstride 和 cstride 分别代表行和列的跨度; cmap 曲面颜色
    ax.plot_surface(x,y,z,rcount=1000,ccount=1000,cmap='rainbow')
    plt.show()

# 画等高线图
def drawContour(x,y,z):
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

os.chdir(r'D:\00-华为科技\02-深圳IOC\02-市民服务分析报告\V4')
locs = pd.read_excel('locs.xlsx',0)
area = pd.read_excel('locs.xlsx',1)
print(locs.head())
print(area.head())

# n = np.linspace(0,len(locs))
x = locs['lat'].values
y = locs['lng'].values
z = np.diag(locs['num'].values)
x,y = np.meshgrid(x,y)
draw3D(x,y,z)
