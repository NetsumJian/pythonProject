import numpy as np

# np.zeros(shape, dtype=None, order='C')
# 创建一个形状为shape 的全零数组, dtype为数据类型,order=C 代表行优先, order=F 代表列优先
print(np.zeros([2,2]))

# np.ones(shape,dtype=None,order='C')
# 创建一个全 1 的数组, 和np.zeros类似
print(np.ones([2,2]))

# np.eye(N, M=None, k=0, dtype=float, order='C')
# 生成一个对角矩阵,N为行数,M为列数,k为对角索引,0代表主对角线
k = np.linspace(0,8)
print(np.eye(3,k=0))

# np.empty(shape, dtype=None, order='C')
# 生成一个未初始化的矩阵
print(np.empty([3,3]))

# np.full(shape, fill_value, dtype=None, order='C')
# 生成一个 fill_value 填充的数组
print(np.full([3,3],k))

# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None,axis=0)
# 生成一个等间隔的数组,start 起始值, stop 终止值, num 数量,endpoint=True表示stop为最后一个值
print(np.linspace(0,100,10))

# np.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0)
# 生成一个数组
a= np.array([1,2,3])
print(a.shape)
print(a.size)
a[0]=5
print(a[0],a[1],a[2])
b = np.array([[1,2,3],[4,5,6]])
print(b[0,0],b[0,1],b[1,0])