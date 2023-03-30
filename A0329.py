# N = int(input('정수 입력: '))
# print(sum(list(map(lambda x: x ** 2, range(1, N + 1)))))
# print(N * (N + 1) * (2 * N + 1) // 6)
#
# a = [0, 1, 5, -5, 17, -20, 50, 6]
# print(a.index(max(a)))
#
# nameList = ['Tom', 'Jerry', 'Mike', 'Tom']
# duplicatedSet = set()
#
# for i, name in enumerate(nameList):
#     if i != len(nameList) - 1:
#         for j in range(i + 1, len(nameList)):
#             if name == nameList[j]:
#                 duplicatedSet.add(nameList[j])
#
# print(duplicatedSet)

# nameList = ['Tom', 'Jerry', 'Mike']
# partnerList = list()
#
# for i, name in enumerate(nameList):
#     if i != len(nameList) - 1:
#         for j in range(i + 1, len(nameList)):
#             partner = ''
#             if name != nameList[j]:
#                 partner += name + ' - ' + nameList[j]
#                 partnerList.append(partner)
#
# print(partnerList)
#
# N, K = map(int, input().split())
#
# res = []
# for i in range(1, N + 1):
#     if N % i == 0:
#         res.append(i)
#
# try:
#     print(res[K - 1])
# except IndexError:
#     print(-1)
#
# T = int(input())
# out = ""
#
# for i in range(0, T):
#     N, s, e, k = map(int, input().split())
#     nums = list(map(int, input().split()))
#     res = []
#     for j in range(s - 1, e):
#         res.append(nums[j])
#     res.sort()
#     if i != T - 1:
#         out += '#' + str(i + 1) + ' ' + str(res[k - 1]) + '\n'
#     else:
#         out += '#' + str(i + 1) + ' ' + str(res[k - 1])
#
# print(out)
#
# def add(n):
#     if n == 1:
#         return 1
#     return n + add(n - 1)
#
#
# print(add(10))
#
# def find(length, vList):
#     if length == 1:
#         return vList[0]
#
#     temp = find(length - 1, vList)
#
#     if temp > vList[length - 1]:
#         return temp
#     else:
#         return vList[length - 1]
#
#
# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(find(len(v), v))
#
# def fb(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fb(n - 1) + fb(n - 2)
#
#
# print(fb(10))

N = int(input())
scores = list(map(int, input().split()))
avg = round(sum(scores) / len(scores))
gaps, res = [], []
for i, score in enumerate(scores):
    gaps.append(abs(avg - score))
for i, gap in enumerate(gaps):
    if min(gaps) == gap:
        res.append(i)
if len(res) == 1:
    print("{0} {1}".format(avg, res[0] + 1))
else:
    for r in res:
        if int(scores[r]) > avg:
            print("{0} {1}".format(avg, r + 1))
            break
