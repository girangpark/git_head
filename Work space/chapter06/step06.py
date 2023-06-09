class Employee :
    name =None
    pay = 0

    def __init__(self, name):
        self.name = name

    def pay_calc(self):
        pass

class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, base, bonus):
        self.pay = base + bonus
        print('총 수령액 : ', format(self.pay, '3,d'),'원')

class Temporay(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        print('총 수령액 : ',format(self.pay, '3,d'), '원')

p = Permanent("이순신")
p.pay_calc(30000000, 200000)

t = Temporay("홍길동")
t.pay_calc(15000, 80)