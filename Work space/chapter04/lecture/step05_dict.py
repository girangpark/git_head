# dict 객체 특징
#변수 = {'키':'값','키':'값':'키':'값'}

dic = dict(key1=100, key2=200, key3=300)
print(dic)

person = {'name':'홍길동', 'age':15,'address':'서울시'}
print(person)
print(person['name'])
print(person['age'])
print(person['address'])
#수정
person['age']=45
print(person)
#삭제
del person['address']
print(person)
#추가
person['pay']=350
print(person)

#요소검사

print(person['age'])
print('age' in person)

for key in person.keys():
    print(key)
for v in person.values():
    print(v)

for i in person.items():
    print(i)

#단어 빈도수 구하기
charset = ['abc', 'code', 'band', 'band', 'abc']

wc = {}

for key in charset:
    wc[key]=wc.get(key,0)+1
print(wc)

