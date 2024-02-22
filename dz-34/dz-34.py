lst = input("Введите ФИО: ").split()
try:
    print(lst[0], end=" ")
    print(lst[1][:2].replace(lst[1][1:2], "."), end=" ")
    print(lst[2][:2].replace(lst[2][1:2], "."))
except IndexError:
    print("Ошибка ввода данных!")
