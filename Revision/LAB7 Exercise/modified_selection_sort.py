def selection_sort(data):
    comparisions = len(data)
    swaps = 1
    comp_list = []
    swaps_list = []
    for pass_num in range(len(data) - 1, 0, -1): #
        position_largest = 0
        comparisions -= 1
        comp_list.append(comparisions)
        for i in range(1, pass_num + 1):
            if data[i] > data[position_largest]:
                position_largest = i
        data[position_largest], data[i] = data[i], data[position_largest]
        swaps_list.append(swaps)

    return (comp_list, swaps_list)

numbers = [6, 4]
result = selection_sort(numbers)
print(result)
