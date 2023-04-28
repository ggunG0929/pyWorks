# 다중 예외 처리
try:
    data = [15, 20, 99, 8, 0]
    x = input("정수 입력(0~4까지 입력): ")
    num = int(x)
    print(data[num])
except IndexError as e:     # 인덱스 요소 접근 에러(4가 넘는 숫자 입력시)
    print(e)
except ValueError as e:     # 문자형 변환 에러(정수가 아닌 문자 입력시)
    print(e)
