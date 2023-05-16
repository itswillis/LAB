def linear_search(words_list):
    for i in range(len(words_list)):
        word = words_list[i]
        if (word[0] in "aeiou") != (word[-1] in "aeiou"):
            return True, i + 1
    return False, len(words_list)

print(linear_search(['summer', 'is', 'over', 'and', 'the', 'hot', 'days', 'are', 'gone']))
print(linear_search(['david', 'michael', 'paul', 'ali']))