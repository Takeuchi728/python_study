dict1 = {'year':'2020', 'month':'8', 'day':'18'}

print(dict1)

print('===============')

for i in dict1:
    print(i)
    print(dict1[i])
    print('---------------')

print('===============')

print(dict1['year'])

print('---------------')

print(dict1.get('year'))
print(dict1.get('Year'))

print('---------------')
print(dict1.get('year', 'NOT FOUND'))
print(dict1.get('kdjf', 'NOT FOUND'))

print('===============')

dict2 = {}
print(dict2)

dict2['year'] = '2020'
dict2['month'] = '8'
dict2['day'] = '22'

print(dict2)

del dict2['day']

print(dict2)

print('===============')

for key, value in dict1.items():
    print(key, value)

print('===============')

print('year' in dict1)
print('years' in dict1)
