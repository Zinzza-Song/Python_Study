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

