import task1
import task2
import task3
import task4
import task5



# Made by Roman Markovets
# variant 17
# 06.06.2024
# version 1.0


#the main function for code testing
def main():
    while True:
        try:
            choice = int(input("1 - information about task, 2 - execute task: "))
            if choice == 1:
                num_of_task = int(input("Enter the number of task: "))
                if num_of_task == 1:
                    print("Given x end eps\nCalculate the number of operations needed to calculate cos(x) by summing up first terms in Talor series\n")
                elif num_of_task == 2:
                    print("Integers are entered until 0 is entered\nOutput the number of odd positive integers among them\n")
                elif num_of_task == 3:
                    print("Given a string, count the number of letters of the Latin alphabet and the number of digits\n")
                elif num_of_task == 4:
                    print("For a constant text, output:\na) the number of words, where first letter is vowel\nb) words, where exist two consecutive equal letters, and their indeces\nc) all the words in alphabetical order\n")
                elif num_of_task == 5:
                    print("Choose the method of initialization of an array, then \na) output the product of even integers with even indeces\nb) output the sum of elements between the first and the last nonzero elements")
                else:
                    print("Your number needs to be between 1 and 5")
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
                    task5.task5()
                else:
                    print("Your number needs to be between 1 and 5")
                    continue

            else:
                print("Your number needs to be between 1 and 2")
                continue

            ans = input("Do you want to continue? 'y' - Yes, otherwise No: ")
            if ans == "y":
                continue
            else:
                break
        except ValueError:
            print("Invalid input")
            continue



if __name__ == "__main__":
    main()