def func(*args, only_odd=False):
    d = []
    for i in args:
        s = str(i)
        res = int(s[::-1])
        if only_odd:
            if i % 2 == 1:
                d.append(res)
        else:
            d.append(res)
    return d


print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))
