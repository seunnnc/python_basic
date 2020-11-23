# 사이트별 비밀번호 만들어 주는 프로그램
# https://제외, 처음 만나는 점 이후 부분 제외, 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e' 갯수 + "!"로 구성

'''
password = ''
url = 'https://naver.com'
url = url.replace('https://','')
index = url.index('.')
siteName = url[:index]
password = siteName[:3] + str(len(siteName)) + str(siteName.count('e')) + "!"
print(password)
'''

url = 'https://naver.com'
url = "https://daum.net"
my_str = url.replace("https://","")
#print(my_str)
my_str = my_str[:my_str.index(".")]
#print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1}입니다.".format(my_str, password))