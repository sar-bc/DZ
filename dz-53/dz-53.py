# Перегрузка операторов

# 24 * 60 * 60 = 86400 - число секунд в сутках

class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    # +
    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    # ==
    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec == other.sec:
            return True
        return False

    # !=
    def __ne__(self, other):
        return not self.__eq__(other)

    # -
    def __sub__(self, other):
        return Clock(self.sec - other.sec)

    # *
    def __mul__(self, other):
        return Clock(self.sec * other.sec)

    # //
    def __floordiv__(self, other):
        return Clock(self.sec // other.sec)

    # %
    def __mod__(self, other):
        return Clock(self.sec % other.sec)

    # >
    def __gt__(self, other):
        return Clock(self.sec > other.sec)

    # <
    def __lt__(self, other):
        return not self.__gt__(other)

    # >=
    def __ge__(self, other):
        return Clock(self.sec >= other.sec)

    # <=
    def __le__(self, other):
        return not self.__ge__(other)


c1 = Clock(600)
c2 = Clock(200)
# ======================
print(f"C1: {c1.get_format_time()}")
c3 = c1 - c2
print(f"C1 - C2: {c3.get_format_time()}")
c3 = c1 * c2
print(f"C1 * C2: {c3.get_format_time()}")
c3 = c1 // c2
print(f"C1 // C2: {c3.get_format_time()}")
c3 = c1 % c2
print(f"C1 % C2: {c3.get_format_time()}")
c1 -= c2
print(f"C1 -= C2: {c1.get_format_time()}")
c1 *= c2
print(f"C1 *= C2: {c1.get_format_time()}")
c1 //= c2
print(f"C1 //= C2: {c1.get_format_time()}")
c3 = c1 % c2
print(f"C1 % C2: {c3.get_format_time()}")

print("*" * 50)
c3 = Clock(800)

print("C3 > C1 ", c3.get_format_time() > c1.get_format_time())
print("C3 >= C1 ", c3.get_format_time() >= c1.get_format_time())
print("C3 < C1 ", c3.get_format_time() < c1.get_format_time())
print("C3 <= C1 ", c3.get_format_time() <= c1.get_format_time())
