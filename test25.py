class TestClass:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #instancemethod
    def sample_instancemethod(self, display_x=True, display_y=True):
        if display_x:
            print('x is {}'.format(self.x))
        if display_y:
            print('y is {}'.format(self.y))

class1 = TestClass(100, 50)
class1.sample_instancemethod(display_x=False)
