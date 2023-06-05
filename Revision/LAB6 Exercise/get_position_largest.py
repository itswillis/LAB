def get_position_of_largest(data, index):

    # a new list up to the index (beginning to index)
    limited = data [0:index+1]

    # get the number of the largest
    largest = max(limited)

    # find the position of largest in original list
    index = data.index(largest)

    return index

numbers = [20, 27, 69, 10, 76, 41]
print(get_position_of_largest(numbers, 2))
