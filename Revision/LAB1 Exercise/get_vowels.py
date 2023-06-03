# list comprehension
def get_vowels(word):
    return [letter for letter in word if letter in 'aeiou']
        

print(get_vowels('solidarity')) # ['o', 'i', 'a', 'i']

    
