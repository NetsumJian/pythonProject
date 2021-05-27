import numpy as np

# reshape()方法改变数组形状
arr3 = np.arange(20).reshape((4,5))
print(arr3)
print(arr3.shape)
print(arr3.mean())
print(arr3.sum())
print(arr3.mean(1))
print(arr3.sum(0))