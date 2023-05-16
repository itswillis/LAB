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
    
word_score1 = WordScore("Electricity!")
print(word_score1)
print(word_score1.get_word(), word_score1.get_score())
word_score2 = WordScore("Water?")
print(word_score2)   

word_score1 = WordScore("beat")
word_score2 = WordScore("beat")
word_score3 = WordScore("beta")
word_score4 = WordScore('standand')
print(word_score1 == word_score2)
print(word_score2 == word_score3)
print(word_score2 < word_score3)
print(word_score3 < word_score4)