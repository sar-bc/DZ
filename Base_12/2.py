def summa(*args):
    res = 0
    lst = []
    for i in args:
        print(i)
        res += i
    aver = res / len(args)
    for j in args:
        if aver > j:
            lst.append(j)
    return aver, lst


print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
