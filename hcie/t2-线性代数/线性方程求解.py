from scipy.linalg import solve
import numpy as np

'''
    10a + 8b + 12c = 10
    4a + 4b + 2c = 8
    2a - 4b - 2c = -5
'''

x = np.array([[10,8,12],[4,4,2],[2,-4,-2]])
y = np.array([10,8,-5])

print(x)
print(y)
print(solve(x,y))