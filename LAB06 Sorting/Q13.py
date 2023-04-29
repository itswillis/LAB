def insertion_single_pass(data, index): 
    value_to_insert = data[index]

    for i in range(index - 1, -1, -1): 
        if data[i] > value_to_insert:
            data[i + 1] = data[i]
        else: 
            data[i + 1] = value_to_insert
            break
    else: 
        data[0] = value_to_insert

numbers = [20, 27, 69, 10, 15, 41]
insertion_single_pass(numbers, 3)
print(numbers)