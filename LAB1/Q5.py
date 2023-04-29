def create_english_spanish_dictionary(english_words, spanish_words):
    dic = {} 
    # for loop iterate through the range assume same length
    for i in range(len(english_words)):
        dic[english_words[i]] = spanish_words[i]
    return dic



# test 
words1 = ['love', 'hello', 'goodbye', 'love']
words2 = ['amor', 'hola', 'adios', 'amor']
a_dict = create_english_spanish_dictionary(words1, words2)
for key in sorted(a_dict.keys()):
    print(key, a_dict[key])