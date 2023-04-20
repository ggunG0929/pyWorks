# 나이가 100세 되는 해의 연도 계산하기
# 현재년도 + (100 - age)
import datetime

age = int(input("나이 입력: "))
now = datetime.date.today()
#print(now.year)
result = now.year + (100 - age)
print(f'100세가 되는 해는 {result}년 입니다.')

"""
import calendar as cal

cal.prcal(2023)
cal.prmonth(2021, 4)    # pr이 print라는 의미
"""
