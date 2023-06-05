def print_elements_backward(numbers):
    rev = reversed(numbers)
    result = ' '.join(str(item) for item in rev)
    print(result)

a_list = [3, 15, 25]
print_elements_backward(a_list)
