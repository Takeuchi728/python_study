print('python', end=' ')
print('.', end = '')
print('com')

f_obj = open('test.txt', 'w')

print('python-izm.com', file=f_obj)

print('Pythonの学習サイト : %s' % 'python-izm.com')
print('Pythonの学習サイト : %s-%s.%s' % ('python', 'izm', 'com'))

test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設 %d 日目！ %s' % (test_int, test_str))

print('Pythonの学習サイト : %s' % 'python-izm.com')
print('Pythonの学習サイト : %s-%s.%s' % ('python', 'izm', 'com'))

test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設 %d 日目！ %s' % (test_int, test_str))
