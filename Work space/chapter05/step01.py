
for i in range(1,6):
    dataset=list(range(1,50))
    print(dataset)

print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))

import statistics
from statistics import variance, stdev
print('평균 = ', statistics.mean(dataset))
print('중위수 = ', statistics.median(dataset))
print('표준 분산 = ', variance(dataset))
print('표본 표준편차 = ', stdev(dataset))

def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')

def userFunc2(x, y):
    print('userFunc2')
    z=x+y
    print('z=',y)

def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')

def userFunc2(x, y):
    print('userFunc2')
    z=x+y
    print('z=',z)
userFunc2(10, 20)

def userFunc3(x, y):
    print('uuserFunc3')
    tot = x+y
    sub = x-y
    mul = x*y
    div = x/y
    return  tot, sub, mul, div
x = int(input('x = '))
y = int(input('y = '))

t, s, m, d = userFunc3(x, y)
print('tot = ', t)
print('sub = ', s)
print('mul = ', m)
print('div = ', d)
