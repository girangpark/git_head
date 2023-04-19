#set 중복 불가
s={1,3,5,3,1}
print(len(s))
print(s)

for a in s:
    print(a, end=' ')

s2 = {3, 6}
print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))

s3 = {1, 3, 5}
print(s3)
s3.add(7)
print(s3)
s3.discard(3)
print(s3)

gender = ['남', '녀', '남', '녀']
setgender = set(gender)
listgender = list(setgender)
print(listgender)
print(listgender[1])