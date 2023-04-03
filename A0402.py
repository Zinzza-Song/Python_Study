# # 동명 이인 찾기
# def find_same_name(a):
#     name_dict = {}
#     for name in a:
#         if name in name_dict:
#             name_dict[name] += 1
#         else:
#             name_dict[name] = 1
#     result = set()
#     for name in name_dict:
#         if name_dict[name] >= 2:
#             result.add(name)
#
#     return result
#
#
# name = ["Tom", "Jerry", "Mike", "Tom"]
# print(find_same_name(name))
#
# name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
# print(find_same_name(name2))
#
#
# # 번호 찾기
# def findNameWithNum(n):
#     stuDic = {39: 'Justin', 14: 'John', 67: 'Mike', 105: 'Summer'}
#
#     if n in stuDic:
#         return stuDic[n]
#     else:
#         return '?'
#
#
# print(findNameWithNum(int(input('번호 입력: '))))
#
# T = int(input())
# res = ''
# for i in range(1, T + 1):
#     s = input().split()
#     reverseStr = s[::-1]
#
#     res += '#' + str(i) + ': ' + " ".join(reverseStr) + '\n'
#
# print(res[:len(res) - 1])
#
# N = int(input())
#
# letters1 = []
# letters2 = []
# res = ''
#
# for _ in range(0, N):
#     letters1.append(input())
#
# for _ in range(0, N - 1):
#     letters2.append(input())
#
# for letter in letters1:
#     if letter not in letters2:
#         res += letter
#         break
#
# print(res)

n = int(input())

dic = {}

for _ in range(0, n):
    k, e = map(int, input().split())
    dic[k] = e

res = 0
for k in dic.keys():
    max_n = 0
    a = k
    while a in dic:
        max_n += 1
        a = dic[a]

    if res <= max_n:
        res = max_n

print(res)
