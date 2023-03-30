# Q1
print('Q1')
a = 'a:b:c:d'
b = "#".join(a.split(":"))
print(b)
print('#' * 20)

# Q2
print('Q2')
a = dict(A=90, B=80)
a['C'] = 70
print(a)
print('#' * 20)

# Q3
# 리스트 a의 주소값이 변경 유무(+는 주솟값이 변경되는 새로운 리스트가 생성되고 extend는 기존 리스트에 추가시킨다.)

# Q4
print('Q4')
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
res = 0
for num in A:
    if num >= 50:
        res += num
print(res)
print('#' * 20)

# Q5
print('Q5')
pv = [0, 1]
res = 0
i = 0
N = int(input('정수 입력: '))
while res < N:
    res = pv[i] + pv[i + 1]
    pv.append(res)
    i += 1
print(pv)
print('#' * 20)

# Q6
print('Q6')
sumList = list(map(int, input('정수 입력: ').split(',')))
print(sum(sumList))
print('#' * 20)

# Q7
print('Q7')
N = int(input('정수 입력: '))
gugudan = list(range(1, 10))
gugudan = list(map(lambda x: x * N, gugudan))
print(gugudan)
print('#' * 20)

# Q8
print('Q8')
with open('abc.txt', 'r') as f:
    data = f.readlines()
    f.close()

data.reverse()

with open('abc.txt', 'w') as f:
    for d in data:
        d = d.strip()
        f.write(d)
        f.write('\n')
    f.close()
print('#' * 20)

# Q9
print('Q9')
with open('sample.txt', 'r') as f:
    data = f.readlines()
    f.close()
numList = []
for d in data:
    numList.append(int(d.strip()))
print(sum(numList) / len(numList))
print('#' * 20)

# Q10
print('Q10')


class Calculator:
    def __init__(self, myList):
        self.myList = myList

    def sum(self):
        print(sum(self.myList))

    def avg(self):
        print(sum(self.myList) / len(self.myList))


cal1 = Calculator([1, 2, 3, 4, 5])
cal1.sum()
cal1.avg()
cal2 = Calculator([6, 7, 8, 9, 10])
cal2.sum()
cal2.avg()
print('#' * 20)

# Q11
# sys 모듈 사용, pythonpath 환경 변수 사용, 현재 디렉터리 사용

# Q12
# 7이 출력 / 인덱스 오류가 발생하여 3이 더해지고 그 후 finally를 타고 4가 더해져서 7이 출력됨

# Q13
print('Q13')


def dashInsert(myStr):
    numbers = list(map(int, myStr))
    result = []
    for i, n in enumerate(numbers):
        result.append(str(n))
        if i < len(numbers) - 1:
            odd = n % 2 == 1
            nextOdd = numbers[i + 1] % 2 == 1
            if odd and nextOdd:
                result.append('-')
            elif not odd and not nextOdd:
                result.append('*')
    return result


print("".join(dashInsert(input())))
print('#' * 20)

# Q14
print('Q14')


def compressStr(myStr):
    temp = ""
    result = []
    for i, c in enumerate(myStr):
        if temp != c:
            result.append(c)
            result.append('1')
            temp = c
        else:
            result[-1] = str(int(result[-1]) + 1)
    return result


print("".join(compressStr(input())))
print('#' * 20)

# Q15
print('Q15')


def duplicatedNum(myList):
    result = []
    for number in myList:
        numList = list(map(lambda x: int(x), number))
        numList.sort()
        if len(numList) != 10:
            result.append('False')
        else:
            for i, n in enumerate(numList):
                if i != n:
                    result.append('False')
                    break
                elif i == 9 and i == n:
                    result.append('True')
    return result


print(duplicatedNum(input().split()))
print('#' * 20)
# Q16
print('Q16')


def morse_code(s):
    morse = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z'
    }
    result = ''
    for i in s.split('  '):
        for j in i.split():
            result += morse[j]
    result += ' '
    return result


s = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'
print(morse_code(s))
print('#' * 20)

# Q17
# a[.]{3,}b -> a....b와 매치됨

# Q18
print('Q18')
import re

p = re.compile('[a-z]+')
m = p.search("5 python")
print(m.start() + m.end())
print('#' * 20)

# Q19
print('Q19')
import re
s = "park 010-9999-9999" \
    "kim 010-9909-7789" \
    "lee 010-8789-7768"

phone = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = phone.sub("\g<1>-####", s)
print(result)
print('#' * 20)

# Q20
print('Q20')
import re
email = re.compile(".*[@].*[.](?=com$|net$).*$")
print(email.match("pahkey@gmailcom"))
print(email.match("kim@daum.net"))
print(email.match("lee@myhome.co.kr"))
print('#' * 20)
