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
    
def my_selection_sort(data):
    for i in range(len(data) - 1, -1, -1):  # start from the end of the list and move left
        max_index = i  # initialize max_index to i.
        for j in range(i):  # traverse through the unsorted part of the list
            if data[max_index] < data[j]:  # we compare data[max_index] and data[j]
                max_index = j  # update max_index if we find a larger element
        data[i], data[max_index] = data[max_index], data[i]  # swap the maximum element with the last element of unsorted part


numbers = [76, 53, 48, 24, 12]
my_selection_sort(numbers)
print(numbers)
