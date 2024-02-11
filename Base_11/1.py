d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}


def func(dic):
    res = 1
    for k, v in dic.items():
        res *= v
    return res


print(func(d))
