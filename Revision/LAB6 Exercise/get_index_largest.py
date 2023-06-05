def get_index_of_largest(numbers, index):
    # get the list of numbers up to the index
    limited = numbers[0:index+1]

    # sort the list

    sorted_limited = sorted(limited)
    
    # get the largest number, largest will be the last element

    largest_number = sorted_limited[-1]

    # find the index of that largest number in the original list
    result = numbers.index(largest_number)

    return result
    
a_list = [3, 15, 25, 37, 45]
print(get_index_of_largest(a_list, 3))
