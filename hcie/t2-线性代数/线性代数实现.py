import numpy as np
import scipy as sp

x = np.arange(12)
print(x.shape)

y = x.reshape(3,4)
print(y.shape)

# 矩阵转置
print(y.T)

# A 矩阵的纵列 = B 矩阵的横列 的乘法运算
print(np.matmul(y,y.T))

# 纵横列数相同的矩阵运算
print(y*y)
print(y+y)

# 求行列式
print(np.linalg.det(y))

