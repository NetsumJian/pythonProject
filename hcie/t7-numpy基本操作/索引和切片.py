import numpy as np

# np.arange([start,] stop[, step,], dtype=None)
# 生成等间隔的数组,类似于python中的range方法
arr = np.arange(10)
arr_slice = arr[5:8]
arr_slice[1] = 999
print(arr_slice)
print(arr)
arr_slice[:] = 14
print(arr_slice)
print(arr)
names = np.array(['bob','will','bob','joe'])
data = np.array([[-3,2,0,-1],[1,2,3,-4],[2.5,1.7,-0.2,1],[-8,-4,9,10]])
print(data[names=='bob'])
print(data[names=='bob',2:])