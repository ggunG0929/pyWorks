# 자리배치
# 입장객 수, 좌석 열, 줄 수
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
'''
print("줄 수:",row)

# 위쪽은 seat 아래쪽은 forfor에서 좌석번호가 입장객수보다 크면 빠져나오도록 수정

row=5
col=5
'''
'''
for i in range(0,row):
    for j in range(1,col+1):
        num=col*i+j
        if num>customer:
            break
        print(f"좌석{num}", end=' ')
    print()
'''
# 10미만의 좌석번호에는 앞에 0을 붙이게 임의로 수정
for i in range(0,row):
    for j in range(1,col+1):
        num=col*i+j
        if num<10:
            print(f"좌석0{num}", end=' ')
        elif num>customer:
            break
        else:
            print(f"좌석{num}", end=' ')
    print()
