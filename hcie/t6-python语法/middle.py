# if 语句
try:
    score = input('please input score :')
    score = float(score)
    if 100 >= score >= 90:
        print('A')
    elif 90 > score >= 80:
        print('B')
    elif 80 > score >= 0:
        print('C')
    else:
        print('D')
except Exception:
    print('error score')

# while 循环
i = 0
while i < 9 :
    i += 1
    if i == 3:
        print('continue ...')
        continue
    if i == 5:
        print('break')
        break
    print(i)

# 自定义函数
def fibs(num):
    res = [0,1]
    for i in range(2,num):
        a = res[i-1] + res[i-2]
        res.append(a)
    return res
fibs(5)

def hello(greeting='hello',name='world'):
    print('%s , %s!' %(greeting,name))
hello()
hello('Greet')
hello('gre','uni')
hello(name='lili')

# 类的基本操作
class Greeter(object):
    def __init__(self,name):
        self.name=name

    def greet(self,loud=False):
        if loud:
            print('hello,%s!'%self.name.upper())
        else:
            print('hello,%s'%self.name)

g = Greeter('lk')
g.greet()
g.greet(loud=True)

# 正则表达式
import re
print(re.match('www','www.huawei.com').span())
print(re.match('com','www.huawei.com'))

print(re.search('huawei','www.huawei.com').span())
pattern = re.compile(r'\d+')
m = pattern.search('www.h2uawei1.co5m').group()
print(m)

# 文件操作
with open('f.txt', 'w') as f:
    f.write('www.huawei.com')

with open('f.txt', 'r') as f:
    print(f.read())