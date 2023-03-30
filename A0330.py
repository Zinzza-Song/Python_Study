# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()
# print(A[K - 1])
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search_recursion(target, start, end, data)


N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
print(binary_search_recursion(M, 0, len(A) - 1, A) + 1)
