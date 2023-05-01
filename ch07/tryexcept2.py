# try ~ except ~ finally 구문

def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("여기는 반드시 수행되는 구간입니다.")    # return 사용시 finally가 먼저 표시, print 사용시 None 발생


print(divide(2, 4))
print(divide(2, 0))
