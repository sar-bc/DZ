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
