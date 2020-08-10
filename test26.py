import datetime

class TestClass:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # class ,method
    @classmethod
    def sample_classmehod(cls, date_diff=0):
        today = datetime.date.today()
        d = today + datetime.timedelta(days=date_diff)
        return cls(d.year, d.month, d.day)

# インスタンス化しないで呼び出し
class1 = TestClass.sample_classmehod()
print(class1.year, class1.month, class1.day)

# インスタンス化しないで呼び出し
class2 = TestClass.sample_classmehod(-10)
print(class2.year, class2.month, class2.day)

# 通常のインスタンス
class3 = TestClass(2000, 1, 1)
print(class3.year, class3.month, class3.day)
