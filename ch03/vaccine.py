# 백신 접종자 분류
birthyear=input("출생년도 입력: ")
age=2023-int(birthyear)+1
print(age)
# 선생님은 year를 따로 빼지 않고 문자형으로 비교하여 if문에서도 숫자에 ""표시를 넣어 문자형으로 비교
if age>=20 and age<=65:
    print("백신 접종 대상")
    year=int(birthyear[-1])%5
    if year==1:
        day="월"
    elif year==2:
        day="화"
    elif year==3:
        day="수"
    elif year==4:
        day="목"
    else:
        day="금"
    print("%s요일 접종"%(day))
else:
    print("백신 미접종 대상\n하반기 일정 확인")
