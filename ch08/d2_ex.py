# 2차원 리스트
d = [
    [10, 20],
    [30, 40],
    [50, 60]
]
"""
# 3행 2열
print(d[0][0])  # 10
print(d[1][1])  # 40
print(d[2][0])  # 50

# [70, 80]을 추가
d.append([70, 80])

# 2차원 리스트 객체 출력
print(d)

# 전체 요소(값) 출력
for x, y in d:
    print(x, y)

# 리스트 이름 = [요소1, 요소2, [값1, 값2]]
e = [7, 3, ['chicken', 'eagle', 'monkey']]

print(e[1])     # 3
print(e[2])     # ['chicken', 'eagle', 'monkey']
print(e[-1])

# eagle 출력
print(e[2][1])
print(e[-1][1])
"""
# 2차원 리스트 - 성적 통계
# 4명의 수학, 영어 과목의 총점과 평균
score = [
    [80, 70],
    [70, 85],
    [60, 90],
    [50, 75]
]

# 개인별 총점과 평균
"""
# 내답
total = 0
for x, y in score:
    total = x + y
    avg = total / len(score[0])
    print(f'총점: {total}, 평균: {avg}')
"""
# 선생님 답
# 수학 - 1열, 영어 - 2열
print("==개인별 총점과 평균==")
print("총점 평균")
n = len(score)  # n은 score의 행 수
for i in range(0, n):
    total = score[i][0] + score[i][1]
    print(total, total / 2)

# 과목별 총점과 평균
# 내 답
"""
total2 = 0
total3 = 0
for x, y in score:
    total2 += x
    total3 += y
print(f'수학총점: {total2}, 수학평균: {total2/len(score)}')
print(f'영어총점: {total3}, 영어평균: {total3/len(score)}')
"""
# 선생님 답
sum_subj = [0, 0]   # sum_subj[0] = 0(수학), sum_subj[1] = 0(영어)
for i in range(0, n):
    sum_subj[0] += score[i][0]  # 수학 합계
    sum_subj[1] += score[i][1]  # 영어 합계
print("==과목별 총점과 평균==")
print(f"\t  수학 영어")     # \t: tab만큼 공백처리인 듯
print("총점: ", sum_subj[0], sum_subj[1])
print("평균:", sum_subj[0]/n, sum_subj[1]/n)
