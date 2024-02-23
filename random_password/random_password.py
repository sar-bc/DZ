# #  генератор паролей
# from random import randint
#
# shortest = 8
# longest = 8
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     res = ""
#     for i in range(randint(shortest, longest)):
#         random_char = chr(randint(min_ascii, max_ascii))
#         res += random_char
#     return res
#
#
# def print_password():
#     for i in range(1, 146):
#         print(random_password())
#
#
# # print("Ваш случайный пароль:", random_password())
# print_password()

import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('количество паролей?'+ "\n")
length = input('длина пароля?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)