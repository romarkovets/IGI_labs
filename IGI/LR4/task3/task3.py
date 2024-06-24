from validators import validate_float_in_range, validate_positive_float
import math
import matplotlib.pyplot as plt
import statistics
import numpy as np


class Function:
    def __init__(self):
        print("Input float x from -10 to 10:")
        self.x = validate_float_in_range(-10.0, 10.0)
        print("Input float eps > 0:")
        self.epsilon = validate_positive_float()
        self.results = []

    @property
    def x_value(self):
        return self.x

    @x_value.setter
    def x_value(self, x):
        self.x = x

    @property
    def epsilon_value(self):
        return self.epsilon

    @epsilon_value.setter
    def epsilon_value(self, epsilon):
        self.epsilon = epsilon

    def calculate(self, x=None):
        self.results = []
        self.values = []
        if x is not None:
            self.x = x
        math_f = math.cos(self.x)
        f = 0
        n = 1
        curr = 1
        while abs(f - math_f) > self.epsilon:
            f += curr
            curr *= (-1) * self.x * self.x / (2 * n - 1) / (2 * n)

            n += 1
            self.results.append(f)
        return f

    # file_plots = "task3/plots.png"
    file_plots = "plots.png"
    def draw_plots(self):
        x = np.arange(-10, 10, 0.1)
        y = np.cos(x)
        z = [self.calculate(el) for el in x]
        plt.title("График функции и ее разложения")
        plt.plot(x, y, x, z)
        plt.legend(['Функция', 'Разложение'])
        plt.savefig(self.file_plots)
        plt.show()

    def average_sequence(self):
        if len(self.results) == 0:
            return None
        return statistics.mean(self.results)

    def median_sequence(self):
        if len(self.results) == 0:
            return None
        return statistics.median(self.results)

    def mode_sequence(self):
        if len(self.results) == 0:
            return None
        return statistics.mode(self.results)

    def variance_sequence(self):
        if len(self.results) == 0:
            return None
        return statistics.variance(self.results)

    def calculate_standard_deviation(self):
        if len(self.results) == 0:
            return None
        return statistics.stdev(self.results)





def task3():
    f = Function()
    f_cos = f.calculate()
    print(f"Вычисленное значение: {f_cos}")
    f.draw_plots()
    print(f"Среднее арифметическое элементов последовательности: {f.average_sequence()}")
    print(f"Медиана последовательности: {f.median_sequence()}")
    print(f"Мода последовательности: {f.mode_sequence()}")
    print(f"Дисперсия последовательности: {f.variance_sequence()}")
    print(f"СКО последовательности: {f.calculate_standard_deviation()}")


if __name__ == "__main__":
    task3()
