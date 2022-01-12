def foo(a: list, b: list) -> None:
    a.extend(b)

xx = ['a','b','c']
yy = ['1','2','3']

foo(xx,yy)

print(xx)
