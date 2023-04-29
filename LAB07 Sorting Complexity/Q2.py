def selection_sort(data):
    compare = [] 
    swaps = []
    for pass_num in range(len(data) - 1, 0, -1):
        position_largest = 0
        compare.append(pass_num)
        for i in range(1, pass_num + 1):
            if data[i] > data[position_largest]:
                position_largest = i
        swaps.append(1)
        data[position_largest], data[i] = data[i], data[position_largest]
    
    return (compare, swaps)


numbers = [6, 4]
result = selection_sort(numbers)
print(result)

numbers = [70, 48, 54, 79, 33]
result = selection_sort(numbers)
print(result)

numbers = [29, 10, 14, 37, 13]
result = selection_sort(numbers)
print(result)