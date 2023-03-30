# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()
# print(A[K - 1])
#
# def binary_search_recursion(target, start, end, data):
#     if start > end:
#         return None
#
#     mid = (start + end) // 2
#
#     if data[mid] == target:
#         return mid
#     elif data[mid] > target:
#         end = mid - 1
#     else:
#         start = mid + 1
#
#     return binary_search_recursion(target, start, end, data)
#
#
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()
# print(binary_search_recursion(M, 0, len(A) - 1, A) + 1)
#
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# C = A + B
# C.sort()
# print(str(C))
#
# N = int(input())
# res = ""
# for i in range(0, N):
#     s = input()
#     if s == s[::-1]:
#         res += '#' + str((i + 1)) + ' YES\n'
#     else:
#         res += '#' + str((i + 1)) + ' NO\n'
# print(res[:len(res) - 1])

n, m = input().split()
m = int(m)

stack = []  # 스택을 이용

for num in n:
    while m > 0 and stack and stack[-1] < num:
        stack.pop()
        m -= 1
    stack.append(num)

while m > 0:  # 남은 자릿수를 제거
    stack.pop()
    m -= 1

print(''.join(stack))
