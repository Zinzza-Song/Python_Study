'''
변수명 정하기
1) 영문과 숫자, _로 이루어진다.
2) 문자나 _로 시작한다.
3) 특수문자를 사용하면 안된다(&, %등)
4) 키워드 사용하면 안된다(if, for 등)
5) 대소문자를 구분
'''

# a = 1
# b = 2
# A = 3
# print(a, b, A)
#
# a, b, c = 3, 2, 1
# print(a, b, c)
#
# a, b = 10, 20
# print(a, b)
#
# a, b = b, a
# print(a, b)
#
# a = 123
# print(type(a))
#
# a = 123.45
# print(type(a))
#
# a = '123.45'
# print(type(a))
#
# print("num")
# a, b, c = 1, 2, 3
# print(a, b, c)
# print("num : ", a, b, c)
#
# print(a, b, c, sep=',')
# print(a, b, c, sep='')
# print(a, b, c, sep='\n')
#
# print(a, end=' ')
# print(b, end=' ')
# print(c)
#
# a = 'Life is too short, You need Python'
# print(a[-1])
# print(len(a))
# # 0 ~ 2
# print(a[0:3])
# # 0 ~ 끝까지
# print(a[0:])
# # 0 ~ 끝까지
# print(a[:len(a)])
#
# print("I eat %d apples" % 3)
# print("I eat %s apples" % 'five')
#
# print('I eat {0} apples'.format(3))
# print('내 이름은 {0}이고 과목은 {1}을 좋아하며 {2}시에 일어납니다.'.format('홍길동', '파이썬', 6))
#
# str = 'I need python'
# print(len(str))
#
# msg = 'It is Computer'
# print(msg.upper())
# print(msg.lower())
# print(msg)
# tmp = msg.upper()
# print(tmp)
# # 인덱스 번호를 찾는다
# print(tmp.find('C'))
# print(tmp.count('C'))
#
# num = 3
# day = 'seven'
# print('%d번 밥을 먹고 %s일 동안 쉬었다.' % (num, day))
# print('{0}번 밥을 먹고 {1}일 동안 쉬었다.'.format(num, day))
#
# p = '801013-1032132'
# print(p[:6])
# print(p[7:])
#
# a = 'Life is too short'
# print(a.split())
#
# a = input('숫자를 입력하세요 : ')
# print(a)
#
# a, b = input('숫자를 입력하세요 : ').split()
# print(a)
# print(b)
# a = int(a)
# b = int(b)
# print(a + b)
# print(type(a))

height, kg = map(float, input('키와 몸무게 입력: ').split())
print('키: {0}cm / 몸무게: {1}kg'.format(height, kg))
