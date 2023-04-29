'''
Write a function called get_position_of_largest(data, index) which takes a list of numbers 
and an index integer as parameters. The function returns the position of the largest 
element from the beginning of the list up to and including the index position. 
You can assume that the list is not empty.
'''

def get_position_of_largest(data, index): 
# SORTED =>[12, 24, 48, 53, 76]
    largest_number = data[0]
    position_of_largest = 0 

    for i in range(1, index+1):
        if data[i] > largest_number:
            largest_number = data[i]
            position_of_largest = i
        
    return position_of_largest

numbers = [76, 53, 48, 24, 12]
print(get_position_of_largest(numbers, 4))

numbers = [53, 48, 24, 76, 28]
print(get_position_of_largest(numbers, 3))