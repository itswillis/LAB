def get_weighted_hash(key, table_size): 
    sum_list = []
    for index, value in enumerate(key):
        index = index + 1
        weight = ord(value)
        sum_weight = index * weight
        sum_list.append(sum_weight)
    
    for _ in range(0, len(sum_list)):
        weighted_sum = sum(sum_list)
    return (weighted_sum % table_size)

print(get_weighted_hash('cat', 13))
print(get_weighted_hash('dog', 13))