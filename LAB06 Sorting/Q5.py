def get_position_of_largest(data, index): 
    largest_number = data[0]
    position_of_largest = 0 

    for i in range(1, index+1):
        if data[i] > largest_number:
            largest_number = data[i]
            position_of_largest = i
        
    return position_of_largest

def selection_single_pass(data, index):
    # Get the position of the largest number here: 
    position_of_largest = get_position_of_largest(data, index)

    # From unsorted => [76, 53, 48, 24, 12]
    # After Single Pass => [12, 53, 48, 24, 76]
    # Selection sort should be from the largest to the smallest, starting from the unsorted on the right
    # We need to get the last index from the list
    # From Python Theory:

    temp = data[position_of_largest] 
    data[position_of_largest] = data[index]
    data[index] = temp

def my_selection_sort(data):
    # run the function 'elements' times	
    for index in range(len(data) - 1, 0, -1 ):
        selection_single_pass(data, index)
    
numbers = [76, 53, 48, 24, 12]
my_selection_sort(numbers)
print(numbers)
    


