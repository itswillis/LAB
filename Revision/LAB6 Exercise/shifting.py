def shifting(data, index):
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

    replicate = data[found_index]
    data[found_index] = replicate
    

numbers = [20, 27, 69, 25, 15, 41]
shifting(numbers, 3)
print(numbers)
