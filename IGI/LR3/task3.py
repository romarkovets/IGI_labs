
# task 3
# computing number of letters of the Latin alphabet and number of digits in the text



def count_letters(text):
    # computing number of letters of the Latin alphabet
    count = 0
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            count += 1
    return count

def count_digits(text):
    # computing number of digits
    count = 0
    for char in text:
        if '0' <= char <= '9':
            count += 1
    return count


def task3():
    #printing result
    text = input("Input the string: ")
    print("Number of letters of the Latin alphabet is", count_letters(text))
    print("Number of digits is", count_digits(text))
    return count_letters(text), count_digits(text)
