# try:
#     x = int(input())
#     y = 10 / x
#     print(y)
# except ZeroDivisionError as e:
#     print(e)

# try:
#     x = int(input())
#     if x % 2 != 0:
#         raise Exception('2의 배수가 아니다')
#     print(x)
# except Exception as e:
#     print('예외 발생', e)

# class E(Exception):
#     def __init__(self):
#         super().__init__('2의 배수 아님')
#
#
# def a(x):
#     try:
#         if x % 2 != 0:
#             raise E
#     except E as e:
#         print('예외 발생', e)
#
#
# a(int(input('정수 입력: ')))

# import datetime as d
#
# t = d.date(2023, 3, 28)
# t += d.timedelta(weeks=1)
# print(t)

# import time as t
# print(t.strftime('%Y/%m/%d/%H/%M'))

# with open("odd.txt", 'w') as f:
#     for i in range(1, 31):
#         if i % 2 != 0:
#             f.write(str(i) + '\n')

# numList = [1, 2, 3, 4]
# resList = []
#
# for i in numList:
#     res = 1
#     for j in numList:
#         if i != j:
#             res *= j
#     resList.append(res)
#
# print(resList)

# class Calculator:
#     def __init__(self, myList):
#         self.myList = myList
#
#     def sum(self):
#         return sum(self.myList)
#
#     def avg(self):
#         return self.sum() / len(self.myList)
#
#
# cal1 = Calculator([1, 2, 3, 4, 5])
# # 15
# print(cal1.sum())
# # 3.0
# print(cal1.avg())
# cal2 = Calculator([6, 7, 8, 9, 10])
# # 40
# print(cal2.sum())
# # 8.0
# print(cal2.avg())

# data = input("리스트를 입력: ")
# print(data)
# data = data.replace("[", "").replace("]", "").replace(",", "").split()
# for item in data:
#     print(item)

# class Area:
#     def __init__(self):
#         self.a = 0
#         self.b = 0
#         self.c = ""
#
#     def set(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get(self):
#         return self.a * self.b
#
#
# a1 = Area()
# a2 = Area()
# a1.set(10, 6, 'red')
# a2.set(4, 4, 'blue')
# print(a1.get())
# print(a2.get())

# import json as j
#
# d = {
#     "a": 40,
#     "b": ("a", 3, 4),
#     "c": "python"
# }
#
# f = "test.json"
# with open(f, 'w') as f:
#     j.dump(d, f)
#
# with open('test.json', 'r') as f:
#     data = j.load(f)
#     print(d["a"])
#     print(d["b"])
#     print(d["c"])

# import re
#
# w = ['orange', 'order', 'october', 'octopus', 'baby', 'busy']
# p = r"oc.*"
# for i in w:
#     if re.match(p, i):
#         print(i)
#
# p = r"b.*.y"
# for i in w:
#     if re.match(p, i):
#         print(i)
