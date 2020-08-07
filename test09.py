list1 = ['python', '-', 'izm']
print(list1)

print('------------')

for i in list1:
    print(i)

print('------------')

list1.append('.com')

print(list1)

print('------------')

# 追加
list1.insert(3, 'www')

print(list1)

print('------------')

# 最初に見つかった物のみ削除
list1.remove('www')

print(list1)

print('------------')

print(list1.pop(1))
print(list1)

# 引数なしだと末尾がポップする
print(list1.pop())
print(list1)

#要素のインデックスの取得
print(list1.index('izm'))

# 要素数の取得
list2 = ['1', '1', '3', '5', '1', '2', '6']

print(list2.count('1'))
