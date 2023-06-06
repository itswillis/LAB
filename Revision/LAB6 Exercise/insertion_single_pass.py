def insertion_single_pass(data, index):
    value_to_insert = data[index]

    # we found the index
    found_index = index

    # find a suitable position of the element
    for i in range(index):
        if data[i] > value_to_insert:
            found_index = i
            break

    j = index

    while j > found_index:
        data[j] = data[j-1]
        j-= 1

    data[found_index] = value_to_insert
    
numbers = [10, 15, 20, 27, 69, 41]
insertion_single_pass(numbers, 5)
print(numbers)
