#문제 01
print("사각형의 넓이와 둘레를 계산합니다.")
width = int(input('가로 = '))
height = int(input('세로 = '))
def Rectangle(a, b):
    pass

    def sjfqdl():
        s = width * height
        return s

    def enffp():
        e = (width + height)*2
        return e

    return sjfqdl, enffp
s, e = Rectangle(width, height)
print("넓이 = ", s())
print("둘레 = ", e())


#문제 02
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print("이름 : ", self.name, end=", ")
        if self.gender == "male":
            print("성별 : 남자")
        elif self.gender == "female":
            print("성별 : 여자")
        else:
            print("성별 : ", self.gender)
        print("나이 : ", self.age)

name = input('이름 : ')
age = int(input('나이 : '))
gender = input('성별(male/female) : ')

person1 = Person(name, gender, age)
person1.display()

#문제 04
class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name

    def pay_calc(self):
        pass

class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, base, bonus, emptype):
        self.pay = base + bonus
        self.emptype = '정규직'

        print('고용형태 :', format(self.emptype))
        print('이름 : ', format(self.name))
        print('급여 : ', format(self.pay,' 3,d'), '원')



class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time, emptype):
        self.pay = tpay * time
        self.emptype = '임시직'

        print('고용형태 :', format(self.emptype))
        print('이름 : ', format(self.name))
        print('급여 : ', format(self.pay, '3,d'), '원')

empType = input("고용형태 선택 (정규직<P>, 임시직<T>) : ")

if empType == 'P' or empType == 'p' :
    name = input("이름 입력 : ")
    base = int(input("기본급 입력 : "))
    bonus = int(input("상여금 입력 : "))
    emp = Permanent(name)
    emp.pay_calc(base, bonus, '정규직')

elif empType == 'T' or empType == 't' :
    name = input("이름 입력 : ")
    tpay = int(input("시간당 급여 입력 : "))
    time = int(input("근무시간 입력 : "))
    emp = Temporary(name)
    emp.pay_calc(tpay, time, '임시직')

else :
    print('='*30)
    print('입력오류')

#문제 5
import test.myCalcPackage.calcModule

x = int(input('x = '))
y = int(input('y = '))

print("Add = ", test.myCalcPackage.calcModule.Add(x, y))
print("Sub = ", test.myCalcPackage.calcModule.Sub(x, y))
print("Mul = ", test.myCalcPackage.calcModule.Mul(x, y))
print("Div = ", test.myCalcPackage.calcModule.Div(x, y))

from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4, 6]


class Scattering:

    def Avg(self, data):
        avg = mean(data)
        return avg

    def var_sd(self, data):
        avg = self.Avg(data)
        diff = [(d - avg) ** 2 for d in data]
        var = sum(diff) / (len(data) - 1)
        sd = sqrt(var)

        return var, sd


s = Scattering()

var_func, Std_func = s.var_sd(x)
print(var_func)
print(Std_func)


