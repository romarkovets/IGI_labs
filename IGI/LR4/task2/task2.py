import re
import zipfile


class Analyzer:
    def __init__(self):
        # self.inputpath = "task2\in.txt"
        # self.outputpath = "task2\out.txt"
        self.inputpath = "in.txt"
        self.outputpath = "out.txt"
        self.text = ""
        self.read_text()

    def read_text(self):
        with open(self.inputpath, newline='') as file:
            self.text = file.read()

    def count_sentences(self):
        return len(re.findall(r"([!?.])", self.text))

    def count_sentences_each_type(self):
        narrative_count = len(re.findall(r"\.", self.text))
        questioning_count = len(re.findall(r"\?", self.text))
        imperative_count = len(re.findall(r"!", self.text))
        return narrative_count, questioning_count, imperative_count

    def count_characters(self):
        characters = re.findall(r'[А-Яа-яa-zA-Z]', self.text)
        return len(characters)

    def count_words(self):
        words = re.findall(r'[А-Яа-яa-zA-Z]+', self.text)
        return len(words)

    def average_length_of_word(self):
        return self.count_characters() / self.count_words()

    def average_length_of_sentence(self):
        return self.count_characters() / self.count_sentences()

    def count_emojis(self):
        emoji_count = len(re.findall(r'[:;]-*([()\[\]])\1*', self.text))
        return emoji_count


class VariantAnalyzer(Analyzer):
    def __init__(self):
        super().__init__()

    def print_words_with_letters_from_f_to_y(self):
        return ', '.join(re.findall(r'\b[f-yF-Y]+\b', self.text))

    def print_costs(self):
        return ', '.join(re.findall(r'\b\d+(?:\.\d{0,2})?\s(?:USD|RUB|EU)\b', self.text))

    def count_words_with_length_smaller_than_7(self):
        return len(re.findall(r'[А-Яа-яa-zA-Z]{1,7}', self.text))

    def smallest_word_starting_with_a(self):
        words = re.findall(r'\ba[А-Яа-яa-zA-Z]*\b', self.text)
        if len(words) == 0:
            return ""
        else:
            word = words[0]
            for element in words:
                if len(element) < len(word):
                    word = element
            return word

    def output_word_sorted_by_length(self):
        words = re.findall(r'[А-Яа-яa-zA-Z]+', self.text)
        return ', '.join(sorted(words, key=len, reverse=True))



    def print_in_console(self):
        print("Number of sentences:", self.count_sentences())
        print("There are {} narrative, {} questioning and {} imperative sentences".format(*self.count_sentences_each_type()))
        print("Average length of a sentence:", self.average_length_of_sentence())
        print("Average length of a word:", self.average_length_of_word())
        print("Number of emojis:", self.count_emojis())
        print("All the words with letters from 'f' to 'y':", self.print_words_with_letters_from_f_to_y(), sep='\n')
        print("All the costs:", self.print_costs(), sep='\n')
        print("Number of words with length < 7:", self.count_words_with_length_smaller_than_7())
        print("The shortest word, starting with 'a':", self.smallest_word_starting_with_a())
        print("All the words in decreasing order of length:", self.output_word_sorted_by_length(), sep='\n')


    def print_in_file(self):
        try:
            with open(self.outputpath, 'w', newline='') as file:
                file.write(f"Number of sentences: {self.count_sentences()}\n")
                file.write("There are {} narrative, {} questioning and {} imperative sentences\n".format(*self.count_sentences_each_type()))
                file.write(f"Average length of a sentence: {self.average_length_of_sentence()}\n")
                file.write(f"Average length of a word: {self.average_length_of_word()}\n")
                file.write(f"Number of emojis: {self.count_emojis()}\n")
                file.write(f"All the words with letters from 'f' to 'y': \n{self.print_words_with_letters_from_f_to_y()}\n")
                file.write(f"All the costs: \n{self.print_costs()}\n")
                file.write(f"Number of words with length < 7: {self.count_words_with_length_smaller_than_7()}\n")
                file.write(f"The shortest word, starting with 'a': {self.smallest_word_starting_with_a()}\n")
                file.write(f"All the words in decreasing order of length: \n{self.output_word_sorted_by_length()}\n")
        except Exception as ex:
            print("File error:", ex)

    def write_to_zip(self):
        try:
            with zipfile.ZipFile(self.outputpath + ".zip", "w") as zip:
                zip.write(self.outputpath)
        except Exception as ex:
            print("Ошибка при архивировании файла:", ex)



def task2():
    analyzer = VariantAnalyzer()
    analyzer.print_in_console()
    analyzer.print_in_file()
    analyzer.write_to_zip()

if __name__ == "__main__":
    task2()
