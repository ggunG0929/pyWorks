# 순차 탐색
# 학생 번호에 해당하는 이름을 순차 탐색으로 찾아
# 돌려주는 함수를 작성하세요(단, 학생번호가 없으면 '?'를 반환함)
def search_list(x):
    n = len(v)
    for i in range(0, n):
        if v[i] == x:
            student = name[i]
            return student
    return "?"

# 선생님답 - 학생번호 리스트도 변수처리하심
# def search_list(a, x):
#     n = len(a)
#     for i in range(0, n):
#         if a[i] == x:
#             return name[i]
#     return '?'


v = [60, 5, 33, 12, 97]     # 학생번호
name = ['이순신', '강감찬', '서희', '안중근', '유관순']

print(search_list(5))
print(search_list(12))
print(search_list(100))
