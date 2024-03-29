# db = {
#     1: {"name": "Игорь", "point": 12},
#     2: {"name": "Валентин", "point": 7},
#     3: {"name": "Виктор", "point": 4},
#     4: {"name": "Григорий", "point": 9},
#     5: {"name": "Дмитрий", "point": 6},
# }
# print(db)
while True:
    try:
        studies = int(input("Кол-во студентов: "))
        break
    except ValueError:
        print("Ошибка ввода. Введите число.")
db = dict()
for i in range(1, studies + 1):
    print(i, end="")
    name = input("-й студент: ")
    while True:
        try:
            point = int(input("Балл: "))
            break
        except ValueError:
            print("Ошибка ввода. Введите балл для студента", name, end="")
            print(".")
    db[i] = {"name": name, "point": point}

# print(db)
print("=" * 20)
average = 0
for k, v in db.items():
    average += v.get("point")
average = average / len(db)
print("Средний балл: ", end="")
print(round(average), end="")
print(". Студенты с баллом выше среднего:")

for k, v in db.items():
    if v.get("point") > average:
        print(v.get("name"))
