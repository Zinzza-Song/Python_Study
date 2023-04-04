# # 소수 판단
# N = int(input())
#
#
# def isPrime(n):
#     if n == 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# primes = 0
# for i in range(1, N+1):
#     if isPrime(i):
#         primes += 1
#
# print(primes)
#
# # 수를 뒤집어서 소수인지 판단
# def reverse(x):
#     return int(str(x)[::-1])
#
#
# def isPrime(x):
#     if x == 1:
#         return False
#     for n in range(2, x):
#         if x % n == 0:
#             return False
#     return True
#
#
# N = int(input())
# li = map(int, input().split())
#
# for i in li:
#     if isPrime(reverse(i)):
#         print(reverse(i), end=' ')

N = int(input())

res = []
li = []
li2 = []
for _ in range(0, N):
    li2.append(0)
li3 = [0, 0]

for i in range(0, N):
    inner = list(map(int, input().split()))
    li.append(inner)
    for idx, k in enumerate(inner):
        li2[idx] += k
    li3[0] += li[i][i]
    li3[1] += li[i][N - 1 - i]
    res.append(sum(inner))

for i in li2:
    res.append(i)

res.append(li3[0])
res.append(li3[1])

print(max(res))












