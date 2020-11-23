#정수, 실수
print(5)
print(-10)
print(3.14)
print(1000000)
print(5+3)
print(10%2)
print(9/3)
print(2-2)
print(2*3)
print((3*12)+4)

#문자
print('haha')
print("ohhhhh")
print('p'*5)    #대박

#boolean
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not False)
print(not True)
print(not(5>10))

#변수
#애완동물 소개
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '입니다')

hobby = '공놀이'    #새로 만들어 줌
print(name + '의 나이는 ' + str(age) + '살이고, 취미는 ' + hobby + '입니다.')
print(name,'은/는 어른인가요? ',  is_adult)

# 숫자나 boolean은 문장안에 넣어줄 때 str()로 넣어준다
# +가 아닌 ,로 해주면 무조건 , 뒤에 한칸 띄어쓰기 되고 str()써줄 필요 없음