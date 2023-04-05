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

N = int(input())
res = []
for _ in range(0, N):
    h, k = map(int, input().split())
    res.append((h, k))
for r in res:
    if any(h > r[0] and w > r[1] for h, w in res):
        res.remove(r)
print(len(res))
