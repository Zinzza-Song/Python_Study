# Q1
print('Q1')
scores = [80, 75, 55]
print('평균: {0}'.format(sum(scores) / len(scores)))
print('#' * 20)

# Q2
print('Q2')
N = 13
if N % 2 == 0:
    print('짝수')
else:
    print('홀수')
print('#' * 20)

# Q3
print('Q3')
pin = '881120-1068234'
yyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print(yyymmdd)
print(num)
print('#' * 20)

# Q4
print('Q4')
pin = '881120-1068234'
print(pin.split('-')[1][0])
print('#' * 20)

# Q5
print('Q5')
a = 'a:b:c:d'
b = a.replace(':', '#')
print(b)
print('#' * 20)

# Q6
print('Q6')
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)
print('#' * 20)

# Q7
print('Q7')
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
print('#' * 20)

# Q8
print('Q8')
a = (1, 2, 3)
a = a + (4,)
print(a)
print('#' * 20)

# Q9
print('Q9')
print("a[[1]] = 'python' -> 리스트는 key값으로 못 들어감")
print('#' * 20)

# Q10
print('Q10')
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)
print('#' * 20)

# Q11
print('Q11')
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)
print('#' * 20)

# Q12
print('Q12')
# a = b = [1, 2, 3]
# a[1] = 4
# print(b)
print('a, b는 동일한 [1, 2, 3]이라는 동일한 리스트 객체를 지칭하고 있어서 a에 변화를 주면 b도 똑같은 영향을 받음')
