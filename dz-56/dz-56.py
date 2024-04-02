import math


class Shape:
    def __init__(self, color):
        self.color = color


class Square(Shape):
    def __init__(self, color, a):
        super().__init__(color)
        self.a = a

    # периметр
    def get_perimeter(self):
        return 4 * self.a

    # площадь
    def get_are(self):
        return self.a * self.a

    # рисование фигуры
    def get_draw(self):
        for i in range(self.a):
            print('*' * self.a)

    def info(self):
        print("===Квадрат===")
        print(f"Сторона: {self.a}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.get_are()}")
        print(f"Периметр: {self.get_perimeter()}")
        self.get_draw()


class Rectangle(Shape):
    def __init__(self, color, a, b):
        super().__init__(color)
        self.a = a
        self.b = b

    # периметр
    def get_perimeter(self):
        return 2 * (self.a + self.b)

    # площадь
    def get_are(self):
        return self.a * self.b

    # рисование фигуры
    def get_draw(self):
        for i in range(self.a):
            for k in range(self.b):
                print("*", end="")
            print("*")

    def info(self):
        print()
        print("===Прямоугольник===")
        print(f"Сторона A: {self.a}")
        print(f"Сторона B: {self.b}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.get_are()}")
        print(f"Периметр: {self.get_perimeter()}")
        self.get_draw()


class Triangle(Shape):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    # периметр
    def get_perimeter(self):
        return (self.a + self.b + self.c) / 2

    # площадь
    def get_are(self):
        return round(math.sqrt(
            self.get_perimeter() * (self.get_perimeter() - self.a) * (self.get_perimeter() - self.b) * (
                    self.get_perimeter() - self.c)), 2)

    # рисование фигуры
    def get_draw(self):
        for i in range(self.c):
            k1 = self.c - 1 - i
            k2 = self.c - 1 + i
            for j in range(k2 + 1):
                print('*' if j >= k1 else ' ', end='')
            print()

    def info(self):
        print()
        print("===Треугольник===")
        print(f"Сторона A: {self.a}")
        print(f"Сторона B: {self.b}")
        print(f"Сторона C: {self.c}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.get_are()}")
        print(f"Периметр: {self.get_perimeter()}")
        self.get_draw()


sq = Square("red", 3)
rc = Rectangle("green", 3, 7)
tr = Triangle("yellow", 11, 6, 6)

lst = [sq, rc, tr]

for x in lst:
    x.info()
