# Q1
N = int(input())
res = ''
for _ in range(0, N):
    a = 0
    nums = list(map(int, input().split()))
    for num in nums:
        if num % 2 == 0:
            a += num
    res += str(a) + '\n'

print(res[:-1])

# Q2
N = int(input())
res = ''
for _ in range(0, N):
    s = input()
    reverse_s = s[::-1]
    if s == reverse_s:
        res += str(1) + '\n'
    else:
        res += str(0) + '\n'
print(res[:-1])


# Q3


def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


N = int(input())
li = []
for _ in range(0, N):
    li.append(int(input()))
merge_sort(li)
for num in li:
    print(num)

# Q4
N = int(input())
res = ''
for _ in range(0, N):
    num = input()
    cnt = 0
    for c in num:
        if c == '7':
            cnt += 1
    res += str(cnt) + '\n'
print(res[:-1])

# Q5
li = list(map(int, input().split()))
target = int(input('타겟: '))


def binary_search(a, x):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


print(binary_search(li, target))

# Q6
names = ['강태성', '강태수', '김준엽', '강태성', '김형록', '유병용', '김태현',
         '이용현', '박종호', '이장군', '전대현', '김태현', '구재경']

# Q6-1
res = 0
for name in names:
    if name[0] == '김' or name[0] == '이':
        res += 1
print(res)

# Q6-2
res = 0
for name in names:
    if name == '김태현':
        res += 1
print(res)

# Q6-3
set_names = set()
duplicate = []
for name in names:
    if name not in set_names:
        set_names.add(name)
    else:
        duplicate.append(name)
print(set_names)

# Q6-4
duplicate.sort()
print(duplicate)
