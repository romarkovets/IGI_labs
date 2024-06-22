from validators import validate_float_in_range, validate_positive_float


class Function:
    def __init__(self):
        print("Input float x from -10 to 10:")
        self.x = validate_float_in_range(-10.0, 10.0)
        print("Input float eps > 0:")
        self.epsilon = validate_positive_float()
        self.results = []
        self.values = []

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





def task3():
    pass


if __name__ == "__main__":
    task3()
