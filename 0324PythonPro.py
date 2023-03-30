# Q1
print('Q1')
N = int(input('정수 입력: '))
result = []
for i in range(1, N + 1):
    if N % i == 0:
        result.append(i)
    i += 1
print(result)
print('#' * 20)

# Q2
print('Q2')
a = [*map(int, input().split())]
print(max(a))
print('#' * 20)

# Q3
print('Q3')
for i in range(4):
    str = ''
    for j in range(5):
        if i == j:
            str += '&'
        else:
            str += '+'
    print(str)
print('#' * 20)

# Q5
print('Q5')
input_str = input('문자열 입력: ')
output_str = ''
output_num = ''
for c in input_str:
    if str.isdigit(c):
        output_num += c
    else:
        output_str += c
print('문자: {0} 정수: {1}'.format(output_str, output_num))
print('#' * 20)

# Q6
print('Q6')
print('$' * 4)
print('#' * 20)

# Q7
print('Q7')
input_str = input('숫자 입력: ')
print('{0}의 자리수'.format(10 ** (len(input_str) - 1)))
print('#' * 20)
