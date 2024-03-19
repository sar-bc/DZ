import math


class Figures:
    count = 0

    @staticmethod
    def area_geron(a, b, c):
        Figures.count += 1
        s = (a + b + c) / 2
        sq = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return sq

    @staticmethod
    def area_triangle(a, b):
        Figures.count += 1
        return 0.5 * a * b

    @staticmethod
    def area_square(a):
        Figures.count += 1
        return a * a

    @staticmethod
    def area_rectangle(a, b):
        Figures.count += 1
        return a * b

    @staticmethod
    def count_method():
        return Figures.count


f = Figures()
print(f"Площадь треугольника по формуле герона (3, 4, 5): {f.area_geron(3, 4, 5)}")
print(f"Площадь треугольника через основание и высоту (6, 7): {f.area_triangle(6, 7)}")
print(f"Площадь квадрата (7): {f.area_square(7)}")
print(f"Площадь прямоугольника (2, 6): {f.area_rectangle(2, 6)}")
print(f"Количество подсчетов площади: {f.count_method()}")

