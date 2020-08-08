set1 = {'python', '-', 'izm'}
# 重複する要素をもたない、順序づけられていない要素の集まり
print(set1)

print('--------------')

for i in set1:
    print(i)

# dictionaly
dict = {}

# set
set2 = {'python'}

# empty set
empty_set = set()

set3 = {'1', '7', '8', '1', '8', '6'}

print('--------------')
print(set3)

set2 = set()
set2.add('thon')
set2.update({'wer', 'you', '456'})

print('--------------')
print(set2)

# removeは指定した要素が存在していない場合はエラー
set2.remove('thon')
set2.discard('456')

print('--------------')
print(set2)

#remove, discard, add, update --> AttributeError
set3 = frozenset({'frozen', 'set', 'www'})

print(set3)
