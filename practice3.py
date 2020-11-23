sentance = '나는 소녀입니다'
print(sentance)

sentance2 = '파이썬 신세계!!'
print(sentance2)

sentance3 = """
나는 학생이고
파이썬 ㄹㅇ신세계
"""
print(sentance3)

print("============")

# 문자열 슬라이싱
jumin = "991230-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0번째 자리부터 2개
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])    # 처음부터 6자리
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리(뒤부터) : " + jumin[-7:])  #맨뒤에서 7번째 부터 끝까지

# 문자열 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))
print(python.replace("Python", "JAVA"))

index = python.index("n")
print(index)

index = python.index("n", index + 1)
print(index)

print(python.find("JAVA"))
#print(python.index("JAVA")) #error발생 
print(python.count("n"))

print()

#문자열 포멧
#print("a" + "b")

# 방법 1
print('나는 %d살입니다.' % 20)
print('나는 %s을 좋아합니다' % '파이썬')
print('Apple은 %c로 시작해요.' % "A")
print()
# %s
print('나는 %s살입니다.' % 20)
print('나는 %s색과 %s색을 좋아합니다.' % ('검정', '흰'))
print()
# 방법 2
print('나는 {}살입니다.'.format(20))
print('나는 {}색과 {}색을 좋아합니다.'.format('검정', '흰'))
print('나는 {0}색과 {1}색을 좋아합니다.'.format('검정', '흰'))
print('나는 {1}색과 {0}색을 좋아합니다.'.format('검정', '흰'))
print()
# 방법 3
print('나는 {age}살이고 {color}색을 좋아합니다'.format(age = 20, color='검정'))
print()
# 방법 4 python3.6이상
age = 20
color = '검정'
print(f'나는 {age}살이고 {color}색을 좋아합니다')

# 탈출문자
print('백문이 불여일견\n백견이 불여일타\n')
#print('저는 '최성은'입니다.')
print('저는 \'최성은\'입니다.\n')

#\\ : 문장내 하나의 \로 바뀜
#print("C:\User\desktop\dev") error
print("C:\\User\\desktop\\dev\n") 

# \r : 커서 맨앞으로 이동
print("Red Apple\rPine\n")

# \b : 백스페이스
print("Redd\bApple\n")

# \t : 탭
print("Red\tApple\n")