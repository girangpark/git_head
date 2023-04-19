# 변수 = [실행문 for 변수 in 열거형객체
# 변수 = [실행문 for 변수 in 열거형객체 if 조건식

x = [2, 4, 1, 5, 7]

lst = [i ** 2 for i in x]
print(lst)

#1~10 -> 2의 배수 추출 -> i*2 -> list 저장
num=list(range(1, 11))
lst2 = [i*2 for i in num if i % 2 == 0]
print(lst2)

t=(10,)
print(t)

t2=(1,2,3,4,5,3)
print(t2)

print(t2[0], t2[1:4], t2[-1])

for i in t2:
    print(i,end=' ')

if 6 in t2:
    print('있음')
else:
    print('없음')

lst = list(range(1,6))
t3 = tuple(lst)
print(t3)

print(len(t3), type(t3))
print(t3,count(3))
print()