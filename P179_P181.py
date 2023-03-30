# Q1
print('Q1')


def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False


print(is_odd(3))
print(is_odd(2))
print('#' * 20)

# Q2
print('Q2')


def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)


print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))
print('#' * 20)

# Q3
print('Q3')
input1 = int(input('첫번째 숫자를 입력하세요:'))
input2 = int(input('첫번째 숫자를 입력하세요:'))

total = input1 + input2
print('두 수의 합은 %s 입니다' % total)
print('#' * 20)

# Q4
# 3번

# Q5
print('Q5')
f1 = open('test.txt', 'w')
f1.write('Life is too short')
f1.close()

f2 = open('test.txt', 'r')
print(f2.read())
print('#' * 20)

# Q6
print('Q6')
user_input = input('저장할 내용을 입력하세요:')
f = open('test.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()
print('#' * 20)

# Q7
print('Q7')
f = open('test.txt', 'r')
body = f.read()
f.close()
body = body.replace('java', 'python')
f = open('test.txt', 'w')
f.write(body)
f.close()
print('#' * 20)
