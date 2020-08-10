class TestClass:

    # static method
    @staticmethod
    def sample_staticmethod(x, y):
        return x + y

# インスタンス化しないで呼び出し
print(TestClass.sample_staticmethod(10, 100))

#インスタンス化してからも呼び出せる
class1 = TestClass()
print(class1.sample_staticmethod(100, 1000))
