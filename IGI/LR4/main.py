import validators
from task1.task1 import task1
from task2.task2 import task2
from task3.task3 import task3
from task4.task4 import task4
from task5.task5 import task5


def main():
    print("""1) Show task description
2) Run the task""")
    case = validators.validate_int_in_range(1, 2)
    print("Choose the task number between 1 and 5")
    task = validators.validate_int_in_range(1, 5)
    match case:
        case 1:
            match task:
                case 1:
                    print("School class methods")
                case 2:
                    print("Methods for text")
                case 3:
                    print("Plots for Tailor's series")
                case 4:
                    print("Inheritance for geometric figures")
                case 5:
                    print("Methods in matrices")
        case 2:
            match task:
                case 1:
                    task1()
                case 2:
                    task2()
                case 3:
                    task3()
                case 4:
                    task4()
                case 5:
                    task5()




if __name__ == "__main__":
    main()
