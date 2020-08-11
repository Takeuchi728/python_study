f = open('read.txt', 'r')

for row in f:
    print(row)

import codecs

f = codecs.open('read.txt', 'w', 'shift_jis')
f.write('書き込みました')

f = open('read.txt', 'r')
for row in f:
    print(row)

f.close()
