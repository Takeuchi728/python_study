print('python')
print("python")

#クォート記号３つで複数行に分けて書く事も出来る
test_str = """
test1
test2
"""
print(test_str)

#文字列の連結
str1 = 'python'
str1 = str1 + '-'
str1 = str1 + 'izm'

print(str1)

str2 = '012'
str2 += '345'
str2 += '67890'

print(str2)

#指定数回数分繰り返す
str3 = '345' * 3

print(str3)

#文字列の変換・置換
integer = 100

print(str(integer) + '円')

print(str1.replace('izm', 'ism'))

str4 = 'Python-Izm.coM'

print(str4.upper())
print(str4.lower())

#文字列の分割・桁ぞろえ

print(str1.split('_'))

str5 = '1234'

#第一引数が桁数、第二引数が埋め込む文字列。ゼロ以外の文字列も埋め込み可。
#文字列を指定せずにゼロで桁埋めはzfillで可
print(str5.rjust(7, '0'))
print(str5.rjust(7))
print(str5.zfill(7))

#文字列の検索
print(str1.startswith('python'))
print(str1.startswith('izm'))

print('z' in str1)
print('s' in str1)

#先頭・末尾の削除
print('----------------------------------')

test_str = '     python-izm.com'
print(test_str)

test_str = test_str.lstrip()
print(test_str)

test_str = test_str.lstrip('python')
print(test_str)


print('----------------------------------')

test_str = 'python-izm.com     '
print(test_str + '/')

test_str = test_str.rstrip()
print(test_str + '/')

test_str = test_str.rstrip("com")
print(test_str)
