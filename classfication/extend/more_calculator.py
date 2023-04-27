from classfication.calculator2 import Calculater2


class MoreCalculater(Calculater2):
    # 2x2x2x2
    def pow(self):
        num = 1
        for i in range(0, self.y):
            num *= self.x
        return num
    """
    def pow(self):
        return self.x ** self.y
    """

    def div(self):
        try:
            return self.x / self.y
        except ZeroDivisionError as e:
            # return "0으로 나눌 수 없습니다."
            return e
    """
        if self.y == 0:
            return 0    # 0으로 종료
        else:
            return self.x / self.y
    """


cal = MoreCalculater(2, 4)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
print(cal.pow())

cal2 = MoreCalculater(5, 0)
print(cal2.add())
print(cal2.sub())
print(cal2.mul())
print(cal2.div())
print(cal2.pow())
