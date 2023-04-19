def Func1(name, *names):
    print(name)
    print(names)

Func1('마크', '테리', '김수현')

from statistics import mean, variance, stdev
def statis(func, *data):

    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return  stdev(data)
    else:
        return 'TypeError'
print('avg=', statis('avg', 1,2,3,4,5))
print('var=', statis('var', 1,2,3,4,5))
print('std=', statis('std', 1,2,3,4,5))

def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)

emp_func('홍길동', 35, addr='서울시', height = 175, weight = 65)

def adder(x, y):
    add = x + y
    return add
print('add = ', adder(10, 20))

print('add = ',(lambda x,y:x+y)(10,20))


x = 50
def local_func(x):
    x += 50

local_func(x)
print(x)

def global_func():
    global x
    x+=50
global_func()
print(x)
