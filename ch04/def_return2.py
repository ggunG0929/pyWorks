# 함수 - 입력기능(매개변수를 통해서)
# 사각형의 넓이 계산 함수
# 내답 선생님은 area w h로 다 지정. 결과도 result로 따로 정의
def calc_area(x,y):
    return x*y

print('사각형의 면적:',calc_area(4,3))
print(f'사각형의 면적: {calc_area(4,3)}')

# 삼각형의 넓이 계산 함수
def tri_area(w,h):
    area=(w*h)/2
    return area

result=tri_area(4,5)
print('삼각형의 면적:',result)
print(f'삼각형의 면적: {result}')

# 정사각형의 면적
'''
size=int(input("숫자를 입력: "))
area=size*size
print(area)
'''
def calc_size(n):
    area=n*n
    return area
print(calc_size(100))
