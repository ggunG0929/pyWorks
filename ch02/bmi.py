# 체질량 지수 = 몸무게 / 키의 제곱
# 키 / 100 -> m로 환산
# 거듭제곱 3**2 = 3X3
# 저체중 20 정상 24 과체중 30 비만

name=input("이름을 입력하세요: ")
weight=float(input("체중(kg)을 입력하세요: "))
height=float(input("키(cm)를 입력하세요: "))
height=height/100 # m로 환산

# 체질량 지수
bmi = (weight / (height**2))
# print(f"{name}님의 bmi는 {bmi:.2f}입니다.") # f스트링 방식
# %포맷 방식: %s - 문자 %f - 실수 %d - 정수
print("%s님의 bmi는 %.2f입니다."%(name,bmi))

if bmi>=30:
    print('비만입니다.')
elif bmi>=24 and bmi<30:
    print('과체중입니다.')
elif bmi>=20 and bmi<24:
    print('정상입니다.')
else:
    print('저체중입니다.')
