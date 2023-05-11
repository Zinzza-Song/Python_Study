# def digit_total(x):
#     sumLi = []
#     for num in x:
#         temp = 0
#         for n in num:
#             temp += int(n)
#         sumLi.append(temp)
#
#     return sumLi.index(max(sumLi))
#
#
# N = int(input())
# li = list(input().split())
#
# print(li[digit_total(li)])

# N = int(input())
# cnt = 0
# for i in range(2, N + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         cnt += 1
#
# print(cnt)

N = int(input())
li = list(input().split())
res = ""

for num in li:
    reverseNum = int("".join(reversed(num)))
    for i in range(2, reverseNum):
        if reverseNum % i == 0:
            break
    else:
        res += str(reverseNum) + " "

print(res)
