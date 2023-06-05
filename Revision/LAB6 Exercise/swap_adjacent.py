def swap_adjacent(numbers, index):
    if numbers[index] > numbers[index+1]:
        temp = numbers[index+1]
        numbers[index+1] = numbers[index]
        numbers[index] = temp

a_list = [3, 15, 25, 37, 45]
swap_adjacent(a_list, 1)
print(a_list)
