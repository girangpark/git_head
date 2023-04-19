class super:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('name : %s, age : %d' % (self.name, self.age))

sup = super('부모', 55)
sup.display()

class sub(super):
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self. gender = gender

    def display(self):
        print('name :  %s, age : %d, gender : %s' %(self.name, self.age, self.gender))

sub = sub('자식', 25, '여자')
sub.display()


class parent:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def display(self):
        print('name : {}, job : {}'.format(self.name, self.job))


p = parent('홍길동', '회사원')
p.display()


class child(parent):
    gender = None

    def __init__(self, name, job, gender):

        super().__init__(name, job)
        self.gender = gender
    def display(self):
        print('name : {}, job : {}, gender : {}'.format(self.name, self.job, self.gender))

chil = child("이순신", '해군 장군', '남자')
chil.display()


