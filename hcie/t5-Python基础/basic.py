# hello world
print('hello world')
# 数值
print(True+False)
print(True or False)
print(5//2)
print(5%2)
print(3**2)
print(5+1.6)
# 字符串
s = 'python'
print(s.split('h'))
print(s.replace('py','PY'))
print(s.upper())
line='aa,bb,cc,dd\n'
print(''.join(['life','is','short']))
hw12='%s,%s,%d' %('hello','world',12)
print(hw12)
# 列表
animals=['cat','dog','monkey']
animals.append('fish')
animals.remove('fish')
animals.insert(1,'fish')
print(animals)
animals.pop(1)
print(animals)
for i in enumerate(animals):
    print(i)
squares=[x*2 for x in animals]
print(squares)
list1=[12,45,32,55]
list1.sort()
print(list1)
list1.reverse()
print(list1)

# 元组
t=(1,2,3)
print(t+(4,5))
t2=(42,)
t1 = (12,45,32,55,[1,0,3])
# t1[0] = 'good'
t1[4][0] =2
print(t1)

# 字典
x={'food':'spam','quantity':4,'color':'pink'}
x1 = dict(food='spam',quantity=4,color='pink')
x2 = dict([('food','spam'),('b','2'),('color','pink')])
d = x.copy()
d['color'] = 'red'
print(x)
print(d)
# print(d['name'])
print(d.get('name'))
print(d.get('name','null'))
print(d.keys())
print(d.items())
d.clear()
print(d)
del(x)
# print(x)
# 集合
s = {'prince','techs'}
print('data' in s)
s.add('data')
print(s)
print(len(s))
s.remove('data')
print(s)
l= [1,3,1,5,3]
print(list(set(l)))
s = frozenset(s)

# 深拷贝和浅拷贝
import copy
d1 = {'name':'lili','age':18,'num':[1,2,8]}
d2 = d1.copy()
d3 = copy.deepcopy(d1)
d1['num'][1] = 6
print('d1: %s'%str(d1),'d2: %s'%str(d2),'d3: %s'%str(d3))
