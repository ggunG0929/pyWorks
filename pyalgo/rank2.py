# 순위 정하기
score = [60, 5, 33, 12, 97, 24]
rank = [0, 0, 0, 0, 0, 0]   # 리스트 요소를 0으로 초기화
n = len(score)
print(n)

# 중첩 for문 - 조건문
for i in range(0, n):
    count = 1   # for문의 로컬(지역) 변수
    for j in range(0, n):
        if score[i] < score[j]:
            count += 1
    rank[i] = count     # 변경된 count를 rank 리스트에 저장
    
print(rank)

"""
i=0 j=0 score[0] < score[0] False count=1     # count = 1
    j=1 score[0] < score[1] False count=1
    j=2 score[0] < score[2] False count=1
    j=3 score[0] < score[3] False count=1
    j=4 score[0] < score[4] True  count=2
    j=5 score[0] < score[5] False count=2(순위 확정)
i=1 j=0 score[1] < score[0] True  count=2
    j=1 score[1] < score[1] False count=2
    j=2 score[1] < score[2] True  count=3
    j=3 score[1] < score[3] True  count=4
    j=4 score[1] < score[4] True  count=5
    j=5 score[1] < score[5] True  count=6(순위 확정)
i=2 j=0 score[2] < score[0] True  count=2
    j=1 score[2] < score[1] False count=2
    j=2 score[2] < score[2] False count=2
    j=3 score[2] < score[3] False count=2
    j=4 score[2] < score[4] True  count=3
    j=5 score[2] < score[5] False count=3(순위 확정)
i=3 j=0 score[3] < score[0] True  count=2
    j=1 score[3] < score[1] True  count=3
    j=2 score[3] < score[2] False count=3
    j=3 score[3] < score[3] False count=3
    j=4 score[3] < score[4] True  count=4
    j=5 score[3] < score[5] True  count=5(순위 확정)

"""

