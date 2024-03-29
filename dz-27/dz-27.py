# s = 0
#
#
# def func1(a, b, c):
#     def func2():
#         s = 2 * (a * b + b * c + a * c)
#         return s
#
#     return func2
#
#
# res1 = func1(2, 4, 6)
# print(res1())
# res2 = func1(5, 8, 2)
# print(res2())
# res3 = func1(1, 6, 8)
# print(res3())


# ==========================
# def func1(a, b, c):
#     s = 0
#
#     def func2():
#         nonlocal s
#         s = 2 * (a * b + b * c + a * c)
#         return s
#
#     return func2
#
#
# res1 = func1(2, 4, 6)
# print(res1())
# res2 = func1(5, 8, 2)
# print(res2())
# res3 = func1(1, 6, 8)
# print(res3())


def outer(a, b, c):
    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


print(outer(2, 4, 6))
print(outer(5, 8, 2))
print(outer(1, 6, 8))
