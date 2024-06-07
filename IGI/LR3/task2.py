
# task 2
# computing number of odd natural numbers


def task2():
    # computing and printing number of odd natural numbers
    x = -1
    ans = 0
    while x != 0:
        try:
            x = int(input("Input an integer number: "))
            if x > 0 and x % 2:
                ans += 1
        except ValueError:
            print("it's not a number, try again")
            continue
    print("There are", ans, "odd natural numbers")