# list comprehension
def correct_errors(data):
    return [0 if i < 0 else i for i in data]

def correct_errors(data):
    return [i for i in data if i > 0 else 0]

print(correct_errors([0, -5, 10, 15, 85, 63, 0, 23]))
