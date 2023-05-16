def get_word_score(word):
    list = []
    result_word = ""
    word = word.lower()
    for char in word:
        if char.isalpha():
            result_word += char
            number = ord(char) - 97
            list.append(number)
    return (result_word, sum(list))
