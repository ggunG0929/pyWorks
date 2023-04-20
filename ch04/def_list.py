# 매개변수가 리스트인 함수
# 리스트 복사를 함수로 이용

def get_list(a):     # v라는 변수는 a와 같음
    a2=[]
    for i in a:
        a2.append(i)
    return a2

v = [1,2,3,4,5]
print(get_list(v))   # [1,2,3,4,5]


