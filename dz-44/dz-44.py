class Car:
    def __init__(self, model, year, product, power, color, price):
        self.model = model
        self.year = year
        self.product = product
        self.power = power
        self.color = color
        self.price = price

    def info(self):
        print(" Данные автомобиля".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.product}\nМощность двигателя: "
                  f"{self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_product(self):
        return self.product

    def set_product(self, product):
        self.product = product

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = power

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


car1 = Car("X7 M50i", "2021", "BMW", "530 л.с.", "white", "1079000")
car1.info()
car1.set_price(1079999)
car1.info()
print(car1.get_price())
print(car1.get_year())
car1.set_year(2023)
print(car1.get_year())
car1.info()

