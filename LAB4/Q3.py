def sum_of_even_numbers(numbers, start_index, end_index):
    try:
        total = 0
        for i in range(start_index, end_index+1):
            if type(numbers[i]) != int:
                print("ERROR: Invalid number!")
                return 0
            if numbers[i] % 2 == 0:
                total += numbers[i]
        return total
    except IndexError:
        print("ERROR: Out of range!")
        return 0

list1 = [1, 2, 3]
print(sum_of_even_numbers(list1, 2, 3))