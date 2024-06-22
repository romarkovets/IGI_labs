def validate_positive_float():
    while True:
        try:
            num = float(input())
            if num < 0:
                raise ValueError
            return num
        except ValueError:
            print("Invalid input: your number needs to be a positive float, try again")


def validate_positive_int():
    while True:
        try:
            num = int(input())
            if num <= 0:
                raise ValueError
            return num
        except ValueError:
            print("Invalid input: your number needs to be a positive integer, try again")


def validate_float_in_range(a, b):
    while True:
        try:
            num = float(input())
            if num < a or num > b:
                raise ValueError
            return num
        except ValueError:
            print("Invalid input: your number needs to be a float between {} and {}, try again".format(a, b))


def validate_int_in_range(a, b):
    while True:
        try:
            num = int(input())
            if num < a or num > b:
                raise ValueError
            return num
        except ValueError:
            print("Invalid input: your number needs to be an integer between {} and {}, try again".format(a, b))

