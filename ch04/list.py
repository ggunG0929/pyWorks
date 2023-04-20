# 리스트
a = [1, 2, 3, 4]

# 리스트(맨뒤)에 5을 추가
a.append(5)

# 5(맨뒤)를 삭제
a.pop()
print(a)


# a리스트의 합계와 평균
sum_v=0
for i in a:
    sum_v += i
print(f'[a]의 합계: {sum_v}')

avg_v=sum_v/len(a)
print(f'[a]의 평균: {avg_v}')

    # 내장함수
print(f'sum = {sum(a)}') # 리스트를 더함

b=(1,2,3,4)              # 튜플
print(sum(b))            # 튜플을 더함

# 리스트 복사
a2=[] # 빈 리스트 a2 생성
'''
a2=a        # 직접 복사
print(a2)
'''
# for ~ in 으로 복사
'''
for i in a:
    a2.append(i)
print(a2)
'''
# a값에서 3의 배수로 복사
for i in a:
    a2.append(3*i)
print(a2)

# a 리스트에서 홀수만 저장
a3=[]
for i in a:
    #if i%2!=0: # 둘 다 같은 의미
    if i%2==1:
        a3.append(i)
print(a3)
