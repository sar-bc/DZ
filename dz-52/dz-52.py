class Student:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"{self.name} => {self.Info.model()}, {self.Info.cpu()}, {self.Info.memory()}")

    class Info:
        @staticmethod
        def model():
            return "HP"

        @staticmethod
        def cpu():
            return "i7"

        @staticmethod
        def memory():
            return "16"


data2 = Student('Roman')
data2.print_info()
data2 = Student('Vladimir')
data2.print_info()
