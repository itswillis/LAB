def linear_search(numbers, target_number):
    for i in range(len(numbers)):
        if numbers[i] == target_number:
            return(True, i+1)
    return (False, i+1)
            
result = linear_search([54, 26, 93, 17, 77, 20], 32)
print('Found: {} Comparisons: {}'.format(result[0], result[1]))
print(type(result))


result = linear_search([93, 54, 78, 18, 61, 13, 36, 42, 16, 60, 58, 92], 61)
print('Found: {} Comparisons: {}'.format(result[0], result[1]))
