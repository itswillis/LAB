def get_longest_column_length(columns_list):
    max_length = 5

    for col in columns_list:
        col_length = len(str(col))
        if col_length > max_length:
            max_length = col_length
            
    return max_length


data = ['Northland region', 'Auckland region', 'Bay of Plenty region']
print(get_longest_column_length(data))
numbers = [23, 2021, 123]
print(get_longest_column_length(numbers))