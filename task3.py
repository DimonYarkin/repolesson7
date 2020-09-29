class Cell:
    def __init__(self, cell_count, name_method=''):
        self.cell_count = int(round(cell_count))
        self.name_method = name_method

    def __str__(self):
        return f"Количество клеток по методу {self.name_method} = {self.cell_count}"

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count, "__add__")

    def __sub__(self, other):
        return Cell(max(self.cell_count, other.cell_count) - min(self.cell_count, other.cell_count), "__sub__")

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count, "__mul__")

    def __truediv__(self, other):
        return Cell(max(self.cell_count, other.cell_count) / min(self.cell_count, other.cell_count), "__truediv__")

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.cell_count / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.cell_count % cells_in_row)}'
        return row


cell_1 = Cell(5, "класса cell_1")
cell_2 = Cell(12, "класса cell_2")
print(cell_1, cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(5))
