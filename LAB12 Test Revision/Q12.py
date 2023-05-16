def get_word_score(word):
    list = []
    result_word = ""
    word = word.lower()
    for char in word:
        if char.isalpha():
            result_word += char
            number = ord(char) - 97
            list.append(number)
    addition = sum(list)
    return (result_word, addition)

class WordScore:
    def __init__(self, word):
        result_word, addition = get_word_score(word)
        self.word = result_word
        self.score = addition

    def get_word(self): 
        return self.word
    def get_score(self):
        return self.score
    def __str__(self):
        return f"{self.word}({self.score})"
    def __eq__(self, other):
        return self.word == other.word
    def __lt__(self, other): 
        return self.score < other.score
    
class FileScore:
    def __init__(self, filename=""):
        self.filename = filename
        try:
            file = open(filename)
            words = file.read().split()
            file.close()
        except FileNotFoundError:
            self.word_scores_list = []
        else:
            self.word_scores_list = [WordScore(word) for word in words]

    def get_filename(self):
        return self.filename

    def get_word_score(self, index):
        return self.word_scores_list[index]


file_score1 = FileScore()
print(len(file_score1.get_filename()))
print(len(file_score1.words_score_list))  # Use the correct attribute name here
