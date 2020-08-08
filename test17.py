value = 2

if value == 1:
    print('value is 1')
elif value == 2:
    print('value is 2')
elif value == 3:
    print('value is 3')
else:
    print('NOT FOUND')

value_1 = 'python'
value_2 = 'izm'

if value_1 == 'Python':
    pass
elif value_1 == 'python' and value_2 == 'izm':
    print('2番目の条件式がTrue')
elif value_1 == "IZM" or value_2 == "PYTHON":
    print('3番目の条件式がTrue')
