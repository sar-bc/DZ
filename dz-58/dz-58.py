class Descriptor:
    def __set_name__(self, owner, name):
        self.__name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"Значение {self.__name} должно быть целым числом")
        instance.__dict__[self.__name] = value


class Point3D:
    x = Descriptor()
    y = Descriptor()
    z = Descriptor()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__)
