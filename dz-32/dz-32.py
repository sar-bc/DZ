def decor(fn):
    def wrap(*args):
        s = ""
        for i in range(len(args)):
            if i < len(args) - 1:
                s = s + str(args[i]) + ", "
            else:
                s = s + str(args[i])
        res = fn(*args) / len(args)
        stroka = f"Сумма чисел {s} = {fn(*args)} \nСреднее арифметическое чисел {s} = {res}"
        return stroka

    return wrap


@decor
def summa(*args):
    x = 0
    for i in range(len(args)):
        x += args[i]
    return x


print(summa(2, 3, 3, 4))
