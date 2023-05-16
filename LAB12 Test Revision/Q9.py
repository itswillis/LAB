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

def read_word_get_sum_score(filename):

    try:
        file = open(filename, 'r')
        data = file.read().split("\n")
        cleaned_words = []
        total_score = 0 
        for line in data:
            line = line.lower()
            words = line.split(" ")

            for word in words:
                cleaned_word = ''.join(char for char in word if char.isalpha())
                if cleaned_word:
                    cleaned_words.append(cleaned_word)

                word_scores = get_word_score(word)
                _, score = word_scores
                total_score += score

        file.close()
        return cleaned_words, total_score
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return
    
read_word_get_sum_score('errors.txt')
