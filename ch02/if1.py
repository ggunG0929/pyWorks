# 조건문
# 삼항 연산자 - 조건 연산자 사용안함
# if문의 콜론(:) 코드 블럭을 의미하고
# 다음 줄에서 4칸 들여쓰기(indent-인덴트) 되어야 함
'''
result=(10<-10) ? 'T':'F' # ?때문에 오류
print(result)
'''

'''
x=10
y=-10

if x<y:
    print("맞음")
else:
    print("틀림")
'''

'''
# 자동차 주행속도가 50km 이상이면 "안전속도 위반!!"
limit_speed = 40
if limit_speed>=50:
    print("안전속도 위반!!")
print("현재 속도는 "+str(limit_speed)+"km입니다.")
'''


# 자동차 주행속도가 50km 이상이면 "안전속도 위반!! 과태료 10만원 부과대상"
# 아니면 "안전 속도 준수"를 출력하는 프로그램
limit_speed = int(input("현재 속도를 입력하세요\n"))
if limit_speed>=50:
    print("안전속도 위반!! 과태료 10만원 부과대상")
else:
    print("안전 속도 준수")
print("현재 속도는 "+str(limit_speed)+"km입니다.")
