def bank_account(bal):
    balance = bal  # 잔액 초기화(10000)

    def getbalance():  # 잔액 확인(getter)
        return balance

    def deposit(money):  # 입금 하기(setter)
        nonlocal balance
        balance += money
        print('%d원 입금후 잔액은 %d원 입니다' % (money, balance))

    def withdraw(money):  # 출금하기
        nonlocal balance
        balance -= money
        if balance > money:
            print('%d 출금후 잔액은 %d원 입니다' % (money, balance))
        else:
            print('잔액이 부족합니다.')

    return getbalance, deposit, withdraw


bal = int(input('최초 계좌의 잔액을 입력하세요 : '))
getbalance, deposit, withdraw = bank_account(bal)
print('현재 계좌 잔액은 %d 입니다' % getbalance())
money = int(input('입금액을 입력하세요 : '))
deposit(money)
money = int(input('출금액을 입력하세요 : '))
withdraw(money)
