# 자리배치
# 입장객 수, 좌석 열, 줄 수
# 입장객 수가 열수로 나누어 떨어지는 경우, 그렇지 않은 경우

customer = int(input("입장객 수 입력: "))
col = int(input("좌석 열 수 입력: "))

몫=customer//col
나머지=customer%col
''' # 선생님은 몫, 나머지 안쓰고 customer col 사용
if 나머지==0:
    row=몫
else:
    row=몫+1
print("줄 수:",row)
'''
if 나머지==0:
    row=int(customer/col)
else:
    row=int(customer/col)+1
print("줄 수:",row)
