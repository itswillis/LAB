def get_longest_length(values_list):
    count = 0
    max_list = []
    for num in values_list:
        if num == 0:
            count = 0
        else:
            count +=1
            max_list.append(count)
    return max(max_list)


result = get_longest_length([3, 6, 12, 0, 0, 9, 10, 5, 5, 0, 2, 1, 3, 0, 9]) #4
print(result)
result = get_longest_length([100])
print(result)
