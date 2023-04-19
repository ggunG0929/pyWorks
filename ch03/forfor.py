# 중첩 for문
# 5행 5열

for i in range(5):
    for j in range(5):
        print('$', end='')
    print()

# 스타(*) 출력
# 삼각형
'''
*
**
***
****
*****
'''
'''
# 내방법
for i in range(1,6):
    print('*'*i)
'''
for i in range(0,5):
    for j in range(0,i+1):
        print('*',end='')
    print()
# 디버깅
'''
i=0, j=0                 *
i=1, j=0 j=1             **
i=2, j=0 j=1 j=2         ***
i=3, j=0 j=1 j=2 j=3     ****
i=4, j=0 j=1 j=2 j=3 j=4 *****
'''
# 숫자배열
'''
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''
# 방법1
for i in range(0,5):
    for j in range(1,6):
        print(5*i+j, end=' ') # 5는 j의 종료값
    print()

#방법2
row=5
col=5
for i in range(0,row):
    for j in range(1,col+1):
        num=col*i+j
        print(num, end=' ')
    print()

