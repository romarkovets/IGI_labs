import random

# task 5
# computing:
# the number of words, starting with vowels
# the number of words with two consecutive equal letters
# all the words in alphabetical order
def InputList(n):
    #inputing elements of array one by one
    array = []
    for _ in range(n):
        element = int(input("Input number: "))
        array.append(element)
    return array


def GenerateList(n):
    #generate random-valued array with given size and given range of elements
    min_element = int(input("Input the minimum of elements: "))
    max_element = int(input("Input the maximum of elements: "))
    array = []
    for _ in range(n):
        element = random.randint(min_element, max_element)
        array.append(element)
    return array


def OutputList(func):
    #the decorator for outputting the array
    def _wrapper(array):
        print("The array is: ", end="")
        for element in array:
            print(element, end=" ")
        print()
        return func(array)
    return _wrapper

@OutputList
def Calculate(array):
    #calculation of product of even numbers with even indeces, and sum of the elements between first and last nonzero elements
    Sum = sum(array)
    mult = 1
    for i in range(len(array)):
        if i % 2 == 0 and array[i] % 2 == 0:
            mult *= abs(array[i])

    left = right = -1
    for i in range(len(array)):
        if array[i] != 0:
            left = i
            break

    for i in reversed(range(len(array))):
        if array[i] != 0:
            right = i
            break

    if left == -1:
        Sum = 0
    elif left == right:
        Sum -= array[left]
    else:
        Sum -= array[right] + array[left]
    return [mult, Sum]





def task5():
    array = []
    while True:
        try:
            n = int(input("Input the number of elements: "))
            choice = int(input("Select type of initialization: 1 - inputing, 2 - random generator"))
            if choice == 1:
                array = InputList(n)
            elif choice == 2:
                array = GenerateList(n)
            else:
                print("Your number needs to be between 1 and 2")
                continue

            break


        except ValueError:
            print("Invalid input")
            continue
    mult, Sum = Calculate(array)
    print("mult = ", mult, " sum = ", Sum)
