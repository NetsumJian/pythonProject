import numpy as np

# np.random.normal(loc=0.0, scale=1.0, size=None)
# 从正态分布中抽取随机样本生成一个数组, loc为分布的平均值,scale为标准差,size为数组形状
samples = np.random.normal(size=(2,2))
print(samples)
print(samples.T)