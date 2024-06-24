import numpy as np
import validators


class NumPyOperations:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = None

    def __str__(self):
        if self.matrix is not None:
            return f"Количество строк: {self.n}, количество столбцов: {self.m}.\nИсходная матрица:\n{self.matrix}"
        else:
            return "Матрица еще не создана."

    def create_matrix(self, min_num=0, max_num=100):
        self.matrix = np.random.randint(min_num, max_num, size=(self.n, self.m))

    def create_zeros(self):
        self.matrix = np.zeros((self.n, self.m))

    def create_ones(self):
        self.matrix = np.ones((self.n, self.m))

    def create_full(self, value):
        self.matrix = np.full((self.n, self.m), value)

    def create_eye(self):
        self.matrix = np.eye(self.n)

    def create_arange(self, start, stop, step=1):
        self.matrix = np.arange(start, stop, step)

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, index, value):
        self.matrix[index] = value

    def __add__(self, other):
        result = NumPyOperations(self.n, self.m)
        if isinstance(other, NumPyOperations):
            result.matrix = self.matrix + other.matrix
        elif isinstance(other, (int, float)):
            result.matrix = self.matrix + other
        else:
            print("Неподдерживаемый тип операнда для сложения.")
            return self.matrix
        return result

    def __sub__(self, other):
        result = NumPyOperations(self.n, self.m)
        if isinstance(other, NumPyOperations):
            result.matrix = self.matrix - other.matrix
        elif isinstance(other, (int, float)):
            result.matrix = self.matrix - other
        else:
            print("Неподдерживаемый тип операнда для вычитания.")
            return self.matrix
        return result

    def __mul__(self, other):
        result = NumPyOperations(self.n, self.m)
        if isinstance(other, NumPyOperations):
            result.matrix = self.matrix * other.matrix
        elif isinstance(other, (int, float)):
            result.matrix = self.matrix * other
        else:
            print("Неподдерживаемый тип операнда для умножения.")
            return self.matrix
        return result

    def __truediv__(self, other):
        result = NumPyOperations(self.n, self.m)
        if isinstance(other, NumPyOperations):
            result.matrix = self.matrix / other.matrix
        elif isinstance(other, (int, float)):
            result.matrix = self.matrix / other
        else:
            print("Неподдерживаемый тип операнда для деления.")
            return self.matrix
        return result

    def __pow__(self, other):
        result = NumPyOperations(self.n, self.m)
        if isinstance(other, NumPyOperations):
            result.matrix = np.power(self.matrix, other.matrix)
        elif isinstance(other, (int, float)):
            result.matrix = np.power(self.matrix, other)
        else:
            print("Неподдерживаемый тип операнда для возведения в степень.")
            return self.matrix
        return result

    def sqrt(self):
        result = NumPyOperations(self.n, self.m)
        result.matrix = np.sqrt(self.matrix)
        return result

    def abs(self):
        result = NumPyOperations(self.n, self.m)
        result.matrix = np.abs(self.matrix)
        return result


class MatrixStatistics(NumPyOperations):
    def __init__(self, n, m):
        super().__init__(n, m)

    def mean(self):
        return np.mean(self.matrix)

    def median(self):
        return np.median(self.matrix)

    def corrcoef(self):
        return np.corrcoef(self.matrix)

    def var(self):
        return np.var(self.matrix)

    def std(self):
        return np.std(self.matrix)

    def get_elemets_exceeding_mean(self):
        mean = np.mean(self.matrix)
        values = []
        for i in range(0, self.n):
            for j in range(0, self.m):
                if self.matrix[i][j] >= mean:
                    values.append(self.matrix[i][j])
        return values

    def num_elements_exceeding_mean(self):
        return len(self.get_elemets_exceeding_mean())

    def std_of_elements_exceeding_mean(self):
        return np.std(self.get_elemets_exceeding_mean())

    def individual_std_of_elements_exceeding_mean(self):
        values = self.get_elemets_exceeding_mean()
        mean = np.mean(values)
        std = 0
        for i in range(0, len(values)):
            std += (values[i] - mean) ** 2
        std /= len(values)
        std = std ** 0.5
        return std



def task5():
    print("Введите количество строк в матрице: ")
    n = validators.validate_positive_int()
    print("Введите количество столбцов в матрице: ")
    m = validators.validate_positive_int()
    arr = MatrixStatistics(n, m)
    arr.create_matrix()
    print(arr)
    print(f"Среднее значение всех элементов матрицы: {arr.mean()}")
    print(f"Медиана матрицы: {arr.median()}")
    print(f"Коэффициент корреляции между элементами матрицы:\n{arr.corrcoef()}")
    print(f"Дисперсии всех элементов матрицы {arr.var()}")
    print(f"Стандартного отклонения всех элементов матрицы: {arr.std()}")
    print(f"Элементы, превосходящие среднее значение матрицы: {arr.get_elemets_exceeding_mean()}")
    print(f"Стандартное отклонение этих элементов: {round(arr.std_of_elements_exceeding_mean(), 2)}")
    print(f"Стандартное отклонение этих элементов (пользовательское): {round(arr.individual_std_of_elements_exceeding_mean(), 2)}")

if __name__ == "__main__":
    task5()
