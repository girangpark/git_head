import random
dataset = []
for i in range(10):
    r = random.randint(1,1000)
    dataset.append(r)
print(dataset)

vmax = vmin = dataset[0]

for i in dataset:
    if vmax < i:
        vmax = i
    if vmin > i:
        vmin = i

print('max = ', vmax, 'min = ', vmin)

dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1) :
    for j in range(i+1, n):
        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i]=dataset[j]
            dataset[j] = tmp
    print(dataset)
print(dataset)

dataset = [5, 10, 18, 22, 35, 55, 75, 103]
value = int(input("검색할 값 입력 : "))

low = 0
high = len(dataset) -1
loc = 0
state = False
while (low <= high):
    mid = (low + high) // 2

    if dataset[mid] > value:
        high = mid - 1
    elif dataset[mid]<value:
        low = mid + 1
    else:
        loc = mid
        state = True
        break
if state:
    print('찾은 위치 : %d 번째' %(loc+1))
else:
    print('찾는 값은 없습니다.')