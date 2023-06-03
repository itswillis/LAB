def get_index_of_smallest(numbers):

    if not numbers:
        return -1

    # we can sort the list first, we always know that the smallest is at index 0
    new_list = sorted(numbers)

    smallest_number = new_list[0]

    for i in range(len(numbers)):
        if numbers[i] == smallest_number:
            return i
    
    
print(get_index_of_smallest([3, 2, 1]))
print(get_index_of_smallest([])) 
        
        
    
