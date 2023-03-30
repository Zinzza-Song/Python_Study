# print(max(list(map(int, input('정수 입력').split()))))


A, B = map(int, input('2 과목 점수 입력: ').split())
res = (lambda a, b: (a + b) / 2)(A, B)
print("{:.1f}".format(res))

alist = list(map(int, input().split()))
alist.sort()
print(alist)
if len(alist) % 2 != 0:
    print(alist[round(len(alist) / 2) - 1])
else:
    res = (alist[(len(alist) / 2) - 1] + alist[(len(alist) / 2)]) / 2

height = list(map(int, input().split()))
total = sum(height)
for i in range(8):
    for j in range(i + 1, 9):
        if total - (height[i] + height[j]) == 100:
            a = height[i]
            b = height[j]
height.remove(a)
height.remove(b)
height.sort()
print(height)
