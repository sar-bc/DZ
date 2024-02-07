sales = {
    "John": [3056, 8463, 8441, 2694],
    "Tom": [4832, 6786, 4737, 3612],
    "Anne": [5239, 4802, 5820, 1859],
    "Fiona": [3904, 3645, 8821, 2451],
}

for key, value in sales.items():
    print(key)
    print("N: ", value[0])
    print("S: ", value[1])
    print("E: ", value[2])
    print("W: ", value[3])
print('=' * 20)
done = False
while True:
    if done:
        break
    name = input("Имя: ")
    if name != "0":
        if name in sales:
            region = input("Регион: ")
            if region == "N":
                print(sales[name][0])
                while True:
                    try:
                        new_val = int(input("Новое значение: "))
                        sales[name][0] = new_val
                        print({'N': sales[name][0], 'S': sales[name][1], 'E': sales[name][2], 'W': sales[name][3]})
                        done = True
                        break
                    except ValueError:
                        print("Значение некорректно. Введите число")
            elif region == "S":
                print(sales[name][1])
                while True:
                    try:
                        new_val = int(input("Новое значение: "))
                        sales[name][1] = new_val
                        print({'N': sales[name][0], 'S': sales[name][1], 'E': sales[name][2], 'W': sales[name][3]})
                        done = True
                        break
                    except ValueError:
                        print("Значение некорректно. Введите число")
            elif region == "E":
                print(sales[name][2])
                while True:
                    try:
                        new_val = int(input("Новое значение: "))
                        sales[name][2] = new_val
                        print({'N': sales[name][0], 'S': sales[name][1], 'E': sales[name][2], 'W': sales[name][3]})
                        done = True
                        break
                    except ValueError:
                        print("Значение некорректно. Введите число")
            elif region == "W":
                print(sales[name][3])
                while True:
                    try:
                        new_val = int(input("Новое значение: "))
                        sales[name][3] = new_val
                        print({'N': sales[name][0], 'S': sales[name][1], 'E': sales[name][2], 'W': sales[name][3]})
                        done = True
                        break
                    except ValueError:
                        print("Значение некорректно. Введите число")
            else:
                print("Такого региона нет")

        else:
            print("Такого имени нет.")
    else:
        break

# sales = {
#     "John": {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     "Tom": {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     "Anne": {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     "Fiona": {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y])
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])
