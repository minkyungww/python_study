from decimal import Decimal
import math
# 파이썬이 기본적으로 가지고 있는 라이브러리는 표준 라이브러리다.
# math. 치면 기능이 드롭다운 형식으로 나옴.

temp = (1 + 2) * 3
print(f'{temp=}')
# temp=9 출력, *가 +보다 우선이지만, 연산 우선순위를 바꾸기 위해서 ()를 사용한다.


# temp = 1 / 0
# 숫자는 0으로 나눌 수 없다: ZeroDivisionError: division by zero

temp = 1.1 + 0.1
print(temp)
# 실수 중에서 2진수로 계산할 수 없는 숫자는 근사값이 나온다.
# 1.2000000000000002

temp = Decimal('1.1') + Decimal('0.1')
print(temp)
# Decimal 을 사용하면 정확한 실수 값을 계산할 수 있다: 1.2
# but 자리수가 한정 되어 있다.
# 1.2

print(f'{temp=}')
# temp=Decimal('1.2')

temp = float(temp)
print(f'{temp=}')
# temp=1.2

temp = 11
temp = bin(temp)
print(temp)
# bin을 사용하면 2진수로 바꿀 수 있다
# 0b1011

temp = 11
temp = oct(temp)
print(f'{temp=}')
# oct를 사용하면 8진수로 바꿀 수 있다
# temp='0o13'

temp = 11
temp = hex(temp)
print(f'{temp=}')
# hex를 사용하면 16진수로 바꿀 수 있다
# 16진수 숫자 : 0 1 2 3 4 5 6 7 8 9 a b c d e f
# 11번이니깐 b가 나옴 (예, a = 10, f = 15)
# temp='0xb'

