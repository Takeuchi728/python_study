import sys

args = sys.argv

print(args)
print('第１引数：' + args[1])
print('第２引数：' + args[2])
print('第３引数：' + args[3])

#
"""
3行目のsys.argvに起動時に設定した引数が格納される
リストで値が返されますが、最初の要素には実行ファイル名が入る
"""
