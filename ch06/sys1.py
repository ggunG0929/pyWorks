# sys 모듈 - system
# 명령프롬프트(명령행에서 인수 사용하기)
import sys

"""
#print(sys.argv)        # 터미널이나 명령프롬프트에서 ch06으로 가서 python sys1.py 쓰고 뒤에 작성되는 것들이 리스트로 만들어짐
print(sys.argv[1:])     # 1번 인덱스부터 추출(슬라이싱)
"""
# 명령행 입력값 연산
args = sys.argv[1:]  # args리스트 생성
print(args)

total = 0
for i in args:
    total += int(i)     # 입력 받은 문자를 숫자형으로 변환해야 함

print("합계:", total)
