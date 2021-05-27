x = [(1,0,3),(1,1,3),(1,2,3),(1,3,2),(1,4,4)]
y = [95.364,97.217205,75.195834,60.105519,49.342380]
epsilon = 0.0001 #迭代阈值,当两次迭代损失函数之差小于该阈值时停止迭代
alpha = 0.01 #学习率
diff = [0,0]
max_iter = 1000
error1 = 0
error0 = 0
cnt = 0
m = len(x)
# 初始化参数
theta0 = 0
theta1 = 0
theta2 = 0
while True :
    cnt += 1
    # 参数迭代计算
    for i in range(m):
        # 拟合函数 y = theta0 * x[0] + theta1*x[1] + theta2*x[2]
        # 计算残差,即拟合函数值 - 真实值
        diff[0] = (theta0 * x[i][0] + theta1 * x[i][1] + theta2 * x[i][2]) - y[i]
        # 梯度 = diff[0] * x[i][j],根据步长 * 梯度更新参数
        theta0 -= alpha * diff[0] * x[i][0]
        theta1 -= alpha * diff[0] * x[i][1]
        theta2 -= alpha * diff[0] * x[i][2]
    # 计算损失函数
    error1 = 0
    for lp in range(len(x)):
        error1 += (y[lp] - (theta0 + theta1*x[lp][1]+theta2*x[lp][2])) **2/2
    # 当两次迭代损失函数之差小于该阈值时停止迭代,跳出循环
    if abs(error1 - error0) < epsilon:
        break
    else:
        error0 = error1
    print('theta0: %f,theta1: %f,theta2: %f,error1: %f,error0: %f' %(theta0,theta1,theta2,error1,error0))

print('Done:theta0: %f,theta1: %f,theta2: %f' %(theta0,theta1,theta2))
print('迭代次数: %d' %cnt)