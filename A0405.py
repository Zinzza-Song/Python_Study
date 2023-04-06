# N = int(input())
# res = []
# for i in range(0, N):
#     dices = list(map(int, input().split()))
#     cnt = 0
#     dice = 0
#     if dices[0] == dices[1]:
#         cnt += 1
#         dice = dices[0]
#     if dices[0] == dices[2]:
#         cnt += 1
#         dice = dices[0]
#     if dices[1] == dices[2]:
#         cnt += 1
#         dice = dices[1]
#     if cnt == 3:
#         res.append(10000 + dice * 1000)
#     elif cnt == 2:
#         res.append(1000 + dice * 100)
#     else:
#         res.append(max(dices) * 100)
# print(max(res))
#
# N = int(input())
# res = []
# for _ in range(0, N):
#     h, k = map(int, input().split())
#     res.append((h, k))
# for r in res:
#     if any(h > r[0] and w > r[1] for h, w in res):
#         res.remove(r)
# print(len(res))

def is_anagram(a, b):
    if len(a) != len(b):
        return False

    a = sorted(a)
    b = sorted(b)

    return a == b


a = input("첫 번째 단어를 입력하세요: ")
b = input("두 번째 단어를 입력하세요: ")

if is_anagram(a, b):
    print("두 단어는 아나그램이다.")
else:
    print("두 단어는 아나그램이 아니다.")