from statistics import mean, variance
from math import sqrt

dataset = [2, 4, 5, 6, 1, 8]

def Avg(data):
    avg = mean(data)
    return avg

print('tkstnfvudrbs = ', Avg(dataset))

def var_sd(data):
    avg=Avg(data)
    diff = [(d - avg)**2 for d in data]

    var = sum(diff)/(len(data)-1)
    sd = sqrt(var)

    return var, sd

v, s =var_sd(dataset)
print(v)
print(s)

#피타고라스
def pytha(s, t):
    a = s**2 - t**2
    b = 2 * s * t
    c = s**2 + t**2
    print(a,b,c)

pytha(4, 3)

#동전 앞면과 뒷면의 난수 확률 분포 함수 정의
import random
def coin(n):
    result = []

    for i in range(n):
        r = random.randint(0, 1)
        if (r == 1):
            result.append(1)#앞면
        else:
            result.append(0)#뒷면
    return  result
print(coin(10))

def mcoin(n):
    cnt = 0
    for i in range(n):
        cnt += coin(1) [0]
    result = cnt / n
    return result

print(mcoin(10))
print(mcoin(30))
print(mcoin(100000))