def func(*args):
    return dict(zip(args, args))


print(func(1, 2, 3, 4))
