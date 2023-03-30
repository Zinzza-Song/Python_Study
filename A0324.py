# a = {'name': 'aa'}
# a['subject'] = 'python'
# print(a)
# print(a['name'])
# print(a.keys())
# print(a.values())
# print(a.items())
# print('name' in a)
# print(a.get('name'))
#
# x = 7
# if x == 7:
#     print('python')
#     print('lucky2')
#
# x = 9
# if x > 0:
#     if x < 10:
#         print('10보다 작은 자연수')
#
# x = 7
# if 0 < x < 10:
#     print('10 보다 작은 자연수')
#
# x = 10
# if x > 0:
#     pass
# else:
#     print('음수')
#
# x = int(input('점수를 입력 하시오 : '))
# if x >= 90:
#     print('A')
# elif x >= 80:
#     print('B')
# elif x >= 70:
#     print('C')
# else:
#     print('F')
#
# A, B = map(int, input('정수 A, B를 입력 하시오: ').split())
# if A > B:
#     print('{0} {1} >'.format(A, B))
# elif A < B:
#     print('{0} {1} <'.format(A, B))
# else:
#     print('{0} {1} =='.format(A, B))
#
# for i in range(10):
#     print(i)
#
# for i in range(1, 10):
#     print(i)
#
# for i in range(10, 0, -1):
#     print(i)
#
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1
#
# i = 1
# while True:
#     print(i)
#     if i == 10:
#         break
#     i += 1
#
# i = 1
# num = int(input('정수 입력: '))
# while i <= num:
#     if i % 2 != 0:
#         print(i)
#     i += 1
#
# sum = 0
# for i in range(1, int(input('정수를 입력 하세요: ')) + 1):
#     sum += i
# print(sum)
#
# res = set()
# num = int(input('정수 입력: '))
# for i in range(1, num + 1):
#     if num % i == 0:
#         res.add(i)
#     i += 1
# print(res)
#
# while True:
#     A, B = map(int, input('정수 두 개 입력: ').split())
#     if A == 0 and B == 0:
#         break
#     print(A + B)
#
# a = [23, 12, 36, 53, 79]
# print(a[:3])
#
# li2 = [n for n in range(1, 6)]
# one = list(map(lambda i: i * 10, li2))
# print(one)
#
# def po(n):
#     re = []
#     for i in n:
#         if i < 0:
#             re.append(i)
#     return re
#
#
# print(po([3, 4, 2, -2, 10, -3]))

def po(n):
    return n < 0


print(list(filter(po, [3, 4, 2, -2, 10, -3])))
print(list(filter(lambda x: x < 0, [3, 4, 2, -2, 10, -3])))
