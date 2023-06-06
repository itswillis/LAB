def linear_search_sorted(numbers, target_number):
    for i in range(len(numbers)):
        if numbers[i] == target_number:
            return(True, i+1)
        elif numbers[i] > target_number:
            return(False, i+1)
    return (False, i+1)


result = linear_search_sorted([2, 3, 5, 6, 7, 8, 9], 4)
print(type(result))
print('Found: {} Equality Comparisons: {}'.format(result[0], result[1]))

result = linear_search_sorted([2, 3, 5, 6, 7, 8, 9], 6)
print('Found: {} Equality Comparisons: {}'.format(result[0], result[1]))
