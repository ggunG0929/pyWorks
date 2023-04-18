# 주석
# 여러줄 주석 : 쌍따옴표나 홑따옴표 3개를 쌍으로 적음

'''
# 자료형 - 숫자, 문자, 불리언, 리스트, 객체 학습
print(12)
print(type(12)) # type()함수 <int - integer(정수)>

print(3.3)
print(type(3.3)) # <float - 실수형>
'''

n=1 # 변수 선언 방법 - 자료형은 생략
print('n=',n,'개') # 콤마(,)는 한 칸 띄움
print('n='+str(n)+'개') # str(숫자) - 문자로 변환

msg="좋은 하루!!"
print('메시지: ',msg)
#print(type(msg)) # <str - 문자형>

num = int('120') # int(문자) - 정수로 변환
print(type(num))

num2 = int(120.7)
print(num2) # 120

# 불리언(참/거짓)
state = True
print(state) # True 첫글자 대문자
print(not state) # False
print(10>11) # False
print(10<11) # True
