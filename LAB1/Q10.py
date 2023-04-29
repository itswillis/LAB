def create_list_of_palindromes(words_list): return [(word, len(word)) for word in words_list if word == word[::-1]]

print(create_list_of_palindromes(['hello', 'civic', 'good', 'job', 'hannah', 'done', 'nun']))