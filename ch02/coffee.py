
# 커피 자동판매기 프로그램
# 돈을 입력하면 커피가 나온다. (커피가격: 400원)
# 돈>커피가격 거스름돈
# 돈<커피가격 돈을 돌려주고 커피는 나오지 않는다
# 커피 수량 소진시 판매중지 (커피 수량: 5개)

coffee=5
while True:
    try:
        money=int(input("돈을 넣어주세요: "))

        if money==400 and coffee!=0:
            print("커피가 나옵니다.")
            coffee-=1
        elif money>400 and coffee!=0:
            print(f"커피가 나오고, 거스름돈 {money-400}원을 돌려받습니다.")
            coffee-=1
        else:
            print("커피가 나오지 않습니다.")
            print(f"남은 커피의 양은 {coffee}개입니다.")
        if coffee==0:
            print(f"커피가 모두 소진되었습니다. 판매를 중지합니다.")
            break
    except:
        pass
