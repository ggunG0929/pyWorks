# 3배로 리스트 복사
a = [1, 2, 3, 4]

a2 = []
for i in a:
    a2.append(3*i)
print(a2)

# 리스트 내포 - for문이 리스트 내부에 포함
a3 = [3*i for i in a]
print(a3)

# a에서 짝수인 숫자만 3을 곱해서 리스트 복사
a4 = []
for i in a:
    if i % 2 == 0:
        a4.append(3*i)
print(a4)

a5 = [3*i for i in a if i % 2 == 0]
print(a5)

# 1부터 10까지 저장하는 리스트
b = [i for i in range(1, 11)]
print(b)

b2 = [i for i in range(1, 11) if i % 2 == 0]
print(b2)
