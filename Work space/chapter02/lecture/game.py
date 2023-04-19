import random

answer = random.randint(1, 101)
guesses = 0
name = input('사용자 이름 : ')
while True:
    guess = int(input('숫자를 입력하세요(1~100) : '))
    guesses +=1
    if guess == answer:
        print(name,'%s 회째 정답'%guesses)
        break
    elif guess>answer:
        print('다운')
    else:
        print('업')
