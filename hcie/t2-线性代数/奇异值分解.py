import numpy as np
import matplotlib.pyplot as plt

words = ['books','dad','stock','value','singular','estate','decomposition']
X = np.array([[0,2,1,0,0,0,0],[2,0,0,1,0,1,0],
              [1,0,0,0,0,0,1],[0,0,1,0,0,0,0],
              [0,1,0,0,0,0,0],[0,0,0,1,1,0,1],
              [0,1,0,0,1,0,0],[0,0,0,0,1,1,1]])
U,s,Vh = np.linalg.svd(X)

# 左奇异矩阵
print('U=',U)
# 奇异值矩阵
print('s=',s)
# 右奇异矩阵
print('V=',Vh)

plt.axis([-0.8,0.2,-0.8,0.8])

for i in range(len(words)):
    plt.text(U[i,0],U[i,1],words[i])

plt.show()