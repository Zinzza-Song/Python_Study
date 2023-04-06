C, N = map(int, input().split())
dogs = []
for _ in range(0, N):
    dogs.append(int(input()))
dogs.sort()
res = 0
temp = 0
while dogs:
    dog = dogs.pop()
    temp += dog
    if temp >= C:
        temp -= dog
    else:
        res = temp
print(res)
