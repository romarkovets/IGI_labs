import task1
import task2
import task3
import task4


def repeat():
    pass


def main():
    while True:
        try:
            choice = int(input("1 - information about task, 2 - execute task: "))
            if choice == 1:
                num_of_task = int(input("Enter the number of task: "))
                if num_of_task == 1:
                    print("given x end eps\nCalculate the number of operations needed to calculate cos(x) by summing up first terms in Talor series\n")
                elif num_of_task == 2:
                    print("integers are entered until 0 is entered\noutput the number of odd positive integers among them\n")
                elif num_of_task == 3:
                    print("given a string, count the number of letters of the Latin alphabet and the number of digits\n")
                elif num_of_task == 4:
                    print("for a constant text, output:\na) the number of words, where first letter is vowel\nb) words, where exist two consecutive equal letters, and their indeces\nc) all the words in alphabetical order\n")

                elif num_of_task == 5:
                    pass
                else:
                    print("your number needs to be between 1 and 5")
                    continue
            elif choice == 2:
                num_of_task = int(input("Enter the number of task: "))
                if num_of_task == 1:
                    task1.task1()
                elif num_of_task == 2:
                    task2.task2()
                elif num_of_task == 3:
                    task3.task3()
                elif num_of_task == 4:
                    task4.task4()

                elif num_of_task == 5:
                    pass
                else:
                    print("your number needs to be between 1 and 5")
                    continue

            else:
                print("Your number needs to be between 1 and 2")
                continue

            repeat()

        except ValueError:
            print("Invalid input")
            continue



if __name__ == "__main__":
    main()