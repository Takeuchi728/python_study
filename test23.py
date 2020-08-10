#慣習的に*args
# タプルとして渡される
def test_func(code, name, *args):
    print(code, name)
    print(args)

test_func(100, 'python', 'com', '33', 4)

#慣習的に**kwargs
#ディクショナリで渡される
def test_func2(code, name, kana, *args, **kwargs):
    print(code, name, kana)
    print(args)
    print(kwargs)

test_func2(
    100, 'python', u'パイソン',
    'JP', 'US',
    email='xxxx', city='Tokyo'
)
