number = 2 + 3 * 4
print(number)
number = number + 2
print(number)

number += 2
print(number)

number *= 2
print(number)

number //= 4
print(number)

number %= 5
print(number)

print('----------------------')

#연산함수
print(abs(-5))
print(pow(4, 2))
print(max(12, 5))
print(min(2, 5))
print(round(3.14))
print(round(4.99))

from math import *
print(floor(4.5))
print(ceil(3.14))
print(sqrt(16)) #제곱근

print('----------------------')
from random import *

print(random())
print(random() * 10)    #0.0 ~ 10.0 미만 임의 값 생성
print(int(random() * 45) + 1)

print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46)) #1~46미만의 랜덤값

print(randint(1, 45))   # 1~45이하 값 출력