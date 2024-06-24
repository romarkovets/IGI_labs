from abc import ABC, abstractmethod
import math
import validators
import matplotlib.pyplot as plt
import numpy as np


class GeometricFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Color:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class TriangleDrawer(GeometricFigure):
    filename = "task4/Triangle.png"
    # filename = "Triangle.png"

    def __init__(self, r, text, color):
        self.r = r
        self.text = text
        self.color = Color(color)

    def __str__(self):
        return f"{Triangle.figure_type}, подпись фигуры: {self.text}"

    def calculate_area(self):
        return 3 / 4 * math.sqrt(3) * self.r * self.r

    def get_info(self):
        return "{} - сторона = {}, цвет = {}, площадь = {}".format(self.figure_type, self.r * math.sqrt(3), self.color.color,
                                                                   self.calculate_area())

    def draw(self):
        fig, ax = plt.subplots(figsize=(5, 5))
        vertices = np.array([[self.r * math.sin(2 * math.pi / 3 * x), self.r * math.cos(2 * math.pi / 3 * x)] for x
                             in range(3)])
        triangle = plt.Polygon(vertices, closed=True, edgecolor="black", facecolor=self.color.color)
        ax.add_patch(triangle)
        ax.set_xlim(-self.r, self.r)
        ax.set_ylim(-self.r, self.r * 1.2)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Треугольник')
        ax.text(0, 0, self.text, ha='center', va='center')
        fig.savefig(self.filename)
        plt.show()


class TriangleDescription:
    figure_type = "Правильный треугольник"


class Triangle(TriangleDescription, TriangleDrawer):
    pass


def task4():
    print("Введите радиус описанной окружности треугольника: ")
    a = validators.validate_positive_float()
    text = input("Введите подпись фигуры: ")
    color = validators.validate_color("Введите цвет треугольника: ")
    triangle = Triangle(a, text, color)
    print(triangle.get_info())
    print(triangle)
    triangle.draw()


if __name__ == "__main__":
    task4()
