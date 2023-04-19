def cal_func(a, b):
    x = a
    y = b

    def plus():
        p = x + y
        return p

    def minus():
        m = x - y
        return m
    return plus, minus

p, m = cal_func(10, 20)
print(p())
print(m())

class calc_class:
    x = y = 0
    def __init__(self, a, b):
        self.x = 10
        self.y = 20
    def plus(self):
        p = self.x + self.y
        return p
    def minus(self):
        m = self.x - self.y
        return m

obj = calc_class(10, 20)

print('plus = ', obj.plus())
print('minus = ', obj.minus())

class car:
    cc = 0
    door = 0
    cartype = None

    def __init__(self, cc, door, cartype):
        self.cc = cc
        self.door = door
        self.cartype = cartype

    def display(self):
        print('자동차는 %d cc이고, 문짝은 %d개, 타입은 %s 이다' % (self.cc, self.door, self.cartype))

car1 = car(2000, 4, '승용차')
car2 = car(3000, 5, 'SUV')

car1.display()
car2.display()