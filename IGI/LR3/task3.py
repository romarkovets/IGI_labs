


def count_letters(text):
    count = 0
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            count += 1
    return count

def count_digits(text):
    count = 0
    for char in text:
        if '0' <= char <= '9':
            count += 1
    return count


def task3():
    text = input("Input the string: ")
    return count_letters(text), count_digits(text)