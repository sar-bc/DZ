
def func(lst):
    count = 0
    if len(lst) == 1:
        if lst[0] < 0:
            count += 1
        else:
            count = 0
    else:
        if lst[0] < 0:
            lst.pop(0)
            count += func(lst) + 1
        else:
            lst.pop(0)
            count = func(lst)

    return count


print("n = ", func([-2, 3, 8, -11, -4, 6]))
