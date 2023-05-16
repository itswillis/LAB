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
    
    def get_total_score(self):
        return sum(word.score for word in self.word_scores_list)
    
    def __str__(self):
        if len(self.word_scores_list) == 0:
            return "No Information!"
        banner = f"{self.filename}:{self.get_total_score()}\n"
        words = "\n".join(str(word) for word in self.word_scores_list)
        return banner + words

file_score1 = FileScore("text.txt")
print(type(file_score1))
print(type(file_score1.get_word_score(0)))
print(file_score1.get_word_score(0))

file_score1= FileScore()
print(len(file_score1.get_filename()))
print(len(file_score1.word_scores_list))

file_score1= FileScore("errors.txt")
print(file_score1.get_filename())
print(len(file_score1.word_scores_list))
