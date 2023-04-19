class Flight:
    def fly(self):
        print('날다, fly 원형 메서드')

class Airplane(Flight):
    def fly(self):
        print('비행기 날다.')

class Bird(Flight):
    def fly(self):
        print('새가 날다.')

class PapaerAirplain(Flight):
    def fly(self):
        print('종이비행기가 날다.')

flight = Flight()
air = Airplane()
bird = Bird()
paper = PapaerAirplain()

flight.fly()

flight = air
flight.fly()

flight = bird
flight.fly()

flight = paper
flight.fly()

lst = [1, 3, 5]
for i, c in enumerate(lst):
    print('색인 : ', i, end=',')
    print('내용 : ', c)

dit = {'name' : '홍길동', 'job': '회사원', 'addr' : '서울시'}
for i, k in enumerate(dit):
    print('순서 : ', i, end=',')
    print('키 : ', k, end=',')
    print('값 : ', dit[k])