def a():
    print('a 함수')
    def b():
        print('b 함수')
    return b

b = a()
b()

data = list(range(1, 101))

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

data = list(range(1,101))
def outer_func(data):
    dataset = data
    def tot():
        tot_val = sum(dataset)
        return tot_val
    def avg():
        avg_val = tot_val / len(dataset)
        return avg_val
    return tot, avg

tot, avg = outer_func(data)

tot_val = tot()
print('tot = ', tot_val)
avg_val = avg()
print('avg = ', avg_val)

from statistics import mean #평균
from statistics import sqrt #제곱근

data = [4, 5, 3.5, 2.5, 6.3, 5.5]

def scattering_func(data):
    dataset = data

    def avg_func():
        avg_val = mean(dataset)
        return avg_val

    def var_func(avg):
        diff = [(data - avg) **2 for data in dataset]
        print(sum(diff))
        var_val = sum(diff)/(len(dataset)-1)
        return var_val

    def std_func(var):
        std_val = sqrt(var)
        return std_val
    return avg_func, var_func, std_func

avg, var, std = scattering_func(data)

print(avg())
print(var(avg()))
print(std( var(avg())))

def main_func(num):
    num_val = num
    def getter():
        return num_val
    def setter(value):
        nonlocal num_val
        num_val = value

    return getter, setter

getter, setter = main_func(100)


print(getter())
setter(200)
print(getter())

def wrap(func):
    def decorated():
        print('반갑')
        func()
        print('잘가')
    return decorated

@wrap

def hello():
    print('hi', '홍길동')
hello()

def counter(n):
    if n == 0:
        return 0
    else :
        counter(n-1)
        print(n,end=' ')

print(counter(0))

counter(5)

def Adder(n) :
    if n == 1:
        return 1
    else :
        result = n + Adder(n-1)

        print(n, end= ' ')
        return result

print('n=1 :',Adder(1))

print('\nn=9 : ', Adder(9))


def starcount(height):
    count = 0
    for i in range(height):
        for j in range(i+1):
            print('*',end='')
            count +=1
        print('')
    return count


height = int(input('height : '))

print('star 개수 %d' %starcount(height))

