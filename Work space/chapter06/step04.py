class account:
    __balance = 0
    __accname = None
    __accno =None

    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accname = name
        self.__accno = no

    def getBalance(self):
        return self.__balance, self.__accname, self.__accno

    def deposit(self, money):
        if money < 0:
            print('금액확인')
            return
        self.__balance += money

    def withraw(self, money):
        if self.__balance < money:
            print('잔액 부족')
            return
        self.__balance -= money

acc = account(100, '홍길동', '125-125-1245-12')

#acc.__balance
bal = acc.getBalance()
print('계좌 정보 : ', bal)

acc.deposit(100)
bal = acc.getBalance()
print('계좌 정보 : ', bal)