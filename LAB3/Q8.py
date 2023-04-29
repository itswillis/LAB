def no_vowels(text):

    for letter in text:
        if letter.lower() in 'aeiou':
            # simplier code, return False immediately after vowels are found
            return False
    return True

print(no_vowels('')) 
print(no_vowels('why'))
print(no_vowels('EUNOIA'))
print(no_vowels('clean'))
print(no_vowels('ant'))

print(no_vowels('dry'))
print(no_vowels('show'))
print(no_vowels('order'))