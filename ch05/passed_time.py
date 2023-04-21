# 지나온 날짜 계산하기
import datetime

day1 = datetime.date(2021, 2, 1)
print(day1)

#today = datetime.date(2023, 4, 21)
today = datetime.date.today
print(today)

passed_time = today - day1
print(passed_time)
print(passed_time.days)
