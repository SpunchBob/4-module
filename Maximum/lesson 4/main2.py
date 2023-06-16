def func(items):
    for i in items:
        yield i

    yield from (i ** 2 for i in items)

for i in func([1, 2, 3, 4]):
    print(i)