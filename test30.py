def func_sample():
    yield('hello')
    yield('good afternoon')
    yield('good night')

f = func_sample()
print(next(f))
print(next(f))
#print(f.next())はpython2系では使用できるが３ではエラー
print(f.__next__())

gen_sample = (i for i in 'hello world !!'.split())

print(gen_sample)
for i in gen_sample:
    print(i)
