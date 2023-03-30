# Q1
print('Q1')


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)
print('#' * 20)

# Q2
print('Q2')


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxLimitCalculator(Calculator):

    def add(self, val):
        super().add(val)
        if self.value > 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)
print('#' * 20)

# Q3
print('Q3')
print(all([1, 2, abs(-3) - 3]))
print(chr(ord('a')) == 'a')
print('#' * 20)

# Q4
print('Q3')
a = list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))
print(a)
print('#' * 20)

# Q5
print('Q5')
print(int('0xea', 16))
print('#' * 20)

# Q6
print('Q6')
a = list(map(lambda x: x * 3, [1, 2, 3, 4]))
print(a)
print('#' * 20)

# Q7
print('Q7')
a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(a) + min(a))
print('#' * 20)

# Q8
print('Q8')
a = 17 / 3
print(round(a, 4))
print('#' * 20)

# Q9
print('Q9')
import sys
numbers = sys.argv[1:]
res = 0
for n in numbers:
    res += int(n)
print(res)
print('#' * 20)
