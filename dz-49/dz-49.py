class Pair:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def side_a(self):
        return self.__a

    @side_a.setter
    def side_a(self, a):
        if a > 0:
            self.__a = a
        else:
            raise ValueError("Сторона A должна быть положительным числом")

    @property
    def side_b(self):
        return self.__b

    @side_b.setter
    def side_b(self, b):
        if b > 0:
            self.__b = b
        else:
            raise ValueError("Сторона B должна быть положительным числом")

    def product(self):
        return self.__a * self.__b

    def sum(self):
        return self.__a + self.__b


class Triangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hypo(self):
        return round((self.side_a ** 2 + self.side_b ** 2) ** 0.5, 2)

    def triangle_info(self):
        print(f"Прямоугольный треугольник ABC ({self.side_a}, {self.side_b}, {self.hypo()})")

    def are(self):
        s = (self.side_a + self.side_b + self.hypo()) / 2
        return round((s * (s - self.side_a) * (s - self.side_b) * (s - self.hypo())) ** 0.5, 2)


t1 = Triangle(5, 8)
print(f"Гипотенуза ABC: {t1.hypo()}")
t1.triangle_info()
print(f"Площадь ABC: {t1.are()}")
print()
print(f"Сумма: {t1.sum()}")
print(f"Произведение: {t1.product()}")
t1.side_a = 9
t1.side_b = 9
print()
print(f"Гипотенуза ABC: {t1.hypo()}")
t1.side_a = 10
t1.side_b = 20
print(f"Гипотенуза ABC: {t1.hypo()}")
print(f"Сумма: {t1.sum()}")
print(f"Произведение: {t1.product()}")
print(f"Площадь ABC: {t1.are()}")
