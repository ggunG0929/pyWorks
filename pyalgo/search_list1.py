# 순차 탐색
# 리스트의 첫번째 자료부터 하나씩 비교하면서 같은 값이 나오면
# 그 위치를 돌려주고(반환), 못 찾으면 -1을 반환함
def search_list(a, x):  # 리스트, 찾는 값
    n = len(a)
    for i in range(0, n):   # 모든 값을 차례로 반복
        if a[i] == x:       # 리스트의 값을 찾는 값과 비교하여 같으면
            return i        # 위치를 반환함
    return -1


def search_list2(a, x):
    same_num = []   # 중복 위치를 저장할 리스트 생성
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            same_num.append(i)
    # 리스트에 찾는 값이 없으면
    if len(same_num) == 0:      # 혹은 if x not in a:
        # return -1
        return "값을 찾을 수 없습니다."
    else:
        return same_num


# 내가 만든 공식(특정된 값의 중복여부를 찾는 것이 아니고 중복된 값이 있는지): 중복된 값이 여러 개일때 보완필요
def search_list3(a):
    n = len(a)
    b = []
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                b.append(i)
                b.append(j)
    if len(b) == 0:
        return "중복된 값이 없습니다."
    else:
        return b


v = [60, 5, 33, 12, 97, 24, 5]

# 매개변수 - 리스트, 찾는 값
# print(search_list(v, 5))    # 1
# print(search_list(v, 12))    # 3
# print(search_list(v, 100))    # -1

# 중복값 위치 찾기
print(search_list2(v, 5))   # [1, 6]
print(search_list2(v, 100))   # -1

print(search_list3(v))   # [1, 6]

