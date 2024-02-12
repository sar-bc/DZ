db = {
    1: {'city': 'Москва', 'counter': 0},
    2: {'city': 'Сочи', 'counter': 0},
}


def func(city):
    for k, v in db.items():
        # print(k, "->", v.get('city'))
        if city == v.get('city'):
            counter = v.get('counter') + 1
            db[k]['counter'] = counter
            return print(v.get('city'), counter)
        else:
            print("Такого города нет")


print(func("Москва"))
print(func("Москва"))
print(func("Сочи"))
print(func("Сочи"))
print(func("Москва"))

