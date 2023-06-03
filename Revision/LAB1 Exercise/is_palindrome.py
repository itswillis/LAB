def is_palindrome(word):
    list = word[::-1]
    for i in range(len(word)):
        if list[i] == word[i]:
            return True
        return False

print(is_palindrome('radar'))
print(is_palindrome('python'))
print(is_palindrome('madam'))
print(is_palindrome('computer'))
