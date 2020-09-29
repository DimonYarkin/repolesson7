class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        strMatrix = ''
        for el in self.matrix:
            strMatrix += " ".join(map(str, el)) + '\n'
        return strMatrix

    def __add__(self, other):
        zip_matrix = zip(self.matrix, other.matrix)
        result_matrix = []
        for el in zip_matrix:
            result_matrix.append([val + el[1][el_1] for el_1, val in enumerate(el[0])])
        return result_matrix


matrix_1 = Matrix([[1, 2, 3], [3, 5, 5], [4, 10, 8]])
matrix_2 = Matrix([[2, 3, 10], [3, 4, 12], [2, 6, 13]])
matrix_result = Matrix(matrix_1 + matrix_2)
print('Первый объект матрица matrix_1')
print(matrix_1)
print("Второй объект матрица matrix_2")
print(matrix_2)
print("Результирующая после сложения matrix_result")
print(matrix_result)
