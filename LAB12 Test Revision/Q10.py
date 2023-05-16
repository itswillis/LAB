def convert_dictionary(scores): 
    result = {}
    for score, words in scores.items():
        for word in words:
            word_len = len(word)
            if word_len not in result:
                result[word_len] = []
            result[word_len].append((word, score))
    return {k: sorted(v) for k, v in result.items()}

data = {24: ['beta', 'beat'], 38: ['fish'], 19: ['of']}
a_dict = convert_dictionary(data)
print(type(a_dict))
for key in sorted(a_dict):
    print(key, a_dict[key])