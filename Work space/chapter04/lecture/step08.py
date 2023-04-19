import random

size = int(input("vector 수 :"))
vector = []
for i in range(size):
    vector.append(random.randint(1,10))
print(vector)
print("vector 크기 : ", len(vector))
