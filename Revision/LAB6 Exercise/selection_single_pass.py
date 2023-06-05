def get_position_of_largest(data, index):

    # a new list up to the index (beginning to index)
    limited = data [0:index+1]

    # get the number of the largest
    largest = max(limited)

    # find the position of largest in original list
    index = data.index(largest)

    return index

def selection_single_pass(data, index):

    # call get_position_of_largest to get the pos of the largest element

    largest_index = get_position_of_largest(data, index)

    # then the largest element in swapped with the lement at the index position

    data[index], data[largest_index] = data[largest_index], data[index]
    

            
    
	
	
	
numbers = [12, 24, 48, 53, 76] # [12, 24, 48, 53, 76]
selection_single_pass(numbers, 3)
print(numbers)
