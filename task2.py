from abc import ABC, abstractmethod


class Сlothes(ABC):
    def __init__(self, size, height, title=""):
        self.size = size
        self.height = height
        self.title = title

    @abstractmethod
    def get_square_coat(self):
        pass

    @abstractmethod
    def get_square_jaket(self):
        pass


class Coat(Сlothes):
    def __init__(self, size, height, title=""):
        super().__init__(size, height, title)
        self.square = self.get_square_coat()

    def get_square_coat(self):
        return round(self.size / 6.5 + 0.5, 2)

    def get_square_jaket(self):
        return 0

    def __str__(self):
        return f'Площадь на {self.title} {self.square}'


class Jacket(Сlothes):
    def __init__(self, size, height, title=""):
        super().__init__(size, height, title)
        self.square = self.get_square_jaket()

    def get_square_coat(self):
        return 0

    def get_square_jaket(self):
        return round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'Площадь на {self.title} {self.square}'


class SumList:
    def __init__(self, arg1):
        self.square = arg1


class Sums:
    def __init__(self):
        self.square = 0;
        self.square_list = []

    def add_square(self, sum_val):
        self.square_list.append(SumList(sum_val))

    @property
    def square_full(self):
        sum_square = self.square
        for el in self.square_list:
            sum_square += el.square
        return f"Общая пощать ткани = {round(sum_square, 2)}"


coat = Coat(4, 0, "пальто")  # Для расчета ткани пальто имеет смысл только размер
jacket = Jacket(0, 2, 'костюм')  # Для расчета ткани костюма имеет смысл только высота

print(coat)
print(jacket)
print(coat.get_square_coat())
print(jacket.get_square_jaket())
sum_obj = Sums()
sum_obj.add_square(coat.square)
sum_obj.add_square(jacket.square)

print(sum_obj.square_full)
