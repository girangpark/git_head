print('프로그램 시작 !!!')

x = [10, 30, 25.2, 'num', 14, 51]

for i in x:
    try :
        y = i**2
        print('i= ', ', y = ', y)
    except :
        print('숫자아님 : ', i)

print("프로그램 종료")

