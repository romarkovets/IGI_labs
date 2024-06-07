import math
# task 1
# computing cos(x) with Tailor series



def get_input():
    #inputing x and eps
    #restart inputing if the values are incorrect
    while True:
        try:
            x = float(input("Input x: "))
            eps = float(input("Input epsilon > 0: "))
            if eps <= 0:
                print("epsilon needs to be greater than 0")
                continue
        except ValueError:
            print("Invalid input")
            continue
        return x, eps



def get_cos(x, eps):
    # calculating the cos(x)
    f = 1
    val = 1
    n = 0
    math_f = math.cos(x)
    while abs(math_f - f) > eps and n < 500:
        n += 1
        val *= -x * x / (2 * n - 1) / (2 * n)
        f += val
    return [x, n, f, math_f, eps]

def task1():
    #printing results
    x, eps = get_input()
    x, n, f, math_f, eps = get_cos(x, eps)
    print("x = ", x, "\t\tn = ", n, "\t\tF(x) = ", f, "\t\tMathF(x) = ", math_f, "\t\teps ", eps, sep='')
