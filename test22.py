#
"""
def func(num1, num2, oprn=1):

    if oprn == 1:
        print('+ start')
        print(num1 + num2)

    elif oprn == 2:
        print('- start')
        print(num1 - num2)

    elif oprn == 3:
        print('* start')
        print(num1 * num2)

    elif oprn == 4:
        print('/ start')
        print(num1 / num2)

    else:
        print('unknown')

func(100, 10)
"""
#関数
def func():
    print('call func')

class TestClass:
    #method
    def test_method():
        print('call test_method')

print('-----------------------')
print(func)
print(TestClass.test_method)

print('-----------------------')
print(type(func))
print(type(TestClass.test_method))

print('-----------------------')
t = TestClass()
print(func)
print(t.test_method)
