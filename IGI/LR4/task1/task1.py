import csv
import pickle
import validators


class Student:
    def __init__(self, name, day_of_birth, month_of_birth, year_of_birth):
        self.name = name
        self.dayOfBirth = day_of_birth
        self.monthOfBirth = month_of_birth
        self.yearOfBirth = year_of_birth


class SchoolClass:
    # csvpath = r"students.csv"
    # picklepath = r"students.txt"
    csvpath = r"task1\students.csv"
    picklepath = r"task1\students.txt"

    def __init__(self, mylist):
        self.listOfStudents = mylist

    def print_students(self):
        print("The list of students: ")
        for student in self.listOfStudents:
            print(student.name, sep="")

    def print_students_by_month(self):
        print("Input the number of month")
        month = validators.validate_positive_int()
        listByMonth = [student for student in self.listOfStudents if student.monthOfBirth == month]
        print("The list of students in month {}: ".format(month))
        for student in listByMonth:
            print(student.name, sep="")

    def add_student(self, student):
        self.listOfStudents.append(student)

    def delete_student(self):
        print("Input the name of a student")
        name = input()
        self.listOfStudents = [student for student in self.listOfStudents if student.name != name]

    def load_from_csv(self):
        self.listOfStudents = []
        with open(self.csvpath, "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.listOfStudents.append(Student(row[0], row[1], row[2], row[3]))

    def save_to_csv(self):
        with open(self.csvpath, "w", newline='') as file:
            writer = csv.writer(file)
            for student in self.listOfStudents:
                writer.writerow([student.name, student.dayOfBirth, student.monthOfBirth, student.yearOfBirth])

    def load_from_pickle(self):
        with open(self.picklepath, 'rb') as file:
            self.listOfStudents = pickle.load(file)

    def save_to_pickle(self):
        with open(self.picklepath, 'wb') as file:
            pickle.dump(self.listOfStudents, file)

    def input_student(self):
        print("Input the name of a student")
        name = input()
        print("Input the day of birth of a student")
        day = validators.validate_positive_int()
        print("Input the month of birth of a student")
        month = validators.validate_positive_int()
        print("Input the year of birth of a student")
        year = validators.validate_positive_int()
        self.add_student(Student(name, day, month, year))


def task1():
    inputfiles = {"Roma": [11, 2, 2005], "Nikita": [11, 10, 2004], "Saske": [17, 2, 2005]}

    myClass = SchoolClass([])
    for (name, date) in inputfiles.items():
        myClass.add_student(Student(name, date[0], date[1], date[2]))

    while True:
        print("""1) Show the list of students in class
2) Add a student to the class
3) Delete a student from the class
4) Load a class from pickle file
5) Load a class from csv file
6) Save a class to pickle file
7) Save a class to csv file
8) Show the list of students of a specific month""")
        case = validators.validate_int_in_range(1, 8)
        match case:
            case 1:
                myClass.print_students()
            case 2:
                myClass.input_student()
            case 3:
                myClass.delete_student()
            case 4:
                myClass.load_from_pickle()
            case 5:
                myClass.load_from_csv()
            case 6:
                myClass.save_to_pickle()
            case 7:
                myClass.save_to_csv()
            case 8:
                myClass.print_students_by_month()


if __name__ == "__main__":
    task1()
