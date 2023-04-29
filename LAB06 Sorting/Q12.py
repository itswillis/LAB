def shifting(data, index):
    value_to_insert = data[index]

    for i in range(index - 1, -1, -1): 
        if data[i] > value_to_insert:
            data[i + 1] = data[i]
        
numbers = [20, 27, 69, 25, 15, 41]
shifting(numbers, 3)
print(numbers)