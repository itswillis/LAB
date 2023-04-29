def get_longest_string_length(dictionary):

    max = 0

    for key in dictionary.keys():
        if len(str(key)) > max:
            max = len(str(key))

    return max

data = {'apple':2, 'banana':6, 'strawberry':3, 'orange':4}
print(get_longest_string_length(data))
a_dict = {23: 'apple', 3456: 'banana', 1: 'strawberry', 56: 'orange'}
print(get_longest_string_length(a_dict))
print(get_longest_string_length({2345678: 'apple', 3456: 'banana', 1:'cat'}))

data = {'input':5, 'template':3, 'data':0}
print(get_longest_string_length(data))