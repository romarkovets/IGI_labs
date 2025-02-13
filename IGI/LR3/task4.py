# task 4
# computing:
# the number of words, starting with vowels
# the number of words with two consecutive equal letters
# all the words in alphabetical order

def words_stasting_with_vowel(text):
    # compute the number of words, starting with vowels
    ans = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split(sep=".", )
    for word in words:
        if word[0] in vowels:
            ans += 1
    return ans

def words_with_equal_consecutive_letters(text):
    # compute the number of words with two consecutive equal letters
    ans = 0
    words = text.split()
    for word in words:
        for i in range(0, len(word) - 1):
            if word[i] == word[i + 1]:
                ans += 1
                break
    return ans

def words_in_alphabetical_order(text):
    # printing all the words in alphabetical order
    words = text.split()
    words.sort()
    for word in words:
        print(word, end=" ")
    print()


def task4():
    #printing results
    text = '''So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.'''
    print("The text:")
    print(text)
    text = text.lower()
    print("The number of words, starting with vowels:", words_stasting_with_vowel(text))
    print("The number of words with two consecutive equal letters:", words_with_equal_consecutive_letters(text))
    print("All the words in alphabetical order:")
    words_in_alphabetical_order(text)


