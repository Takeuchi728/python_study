list1 = ['https', 'www', 'python', '-', 'izm']

print(list1[:])
print(list1[::])

print('--------------')
print(list1[:3])
print(list1[2:])
print(list1[::2])
print(list1[2:3])

print('--------------')
print(list1[-1:]) #末尾から全ての要素
print(list1[:-1]) #末尾までの全ての要素
print(list1[::-1]) #末尾から全ての逆順要素

print('--------------')
list1[1:3] = ('i', 'am')

print(list1)
