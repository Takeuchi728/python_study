import testmod

class_1 = testmod.TestClass()
class_1.test_method('1')

from testmod import TestClass

class_2 = TestClass()
class_2.test_method('2')
