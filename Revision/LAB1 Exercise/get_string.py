# python shortcut
def get_string(words):
    joined = ".".join(words)
    return joined

# long method:
def get_string(words):
    string = ""
    for word in words:
        string = string + "." + word
    return(string[1:])

a_list = ['coderunner', 'auckland', 'ac', 'nz']
print(get_string(a_list))
