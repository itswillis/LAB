def get_folding_hash(key, table_size):
    # break the key integer into a pair of digits (eg 1234 is 12 34)
    # first create an empty list to store 2 characters
    two_char_list = [] 
    key_str = str(key) 
    # secondly iterate through the string 
    for i in range(0, len(key_str), 2):
        two_char = int(key_str[i:i+2])
        two_char_list.append(two_char)
    
    for _ in range(0, len(two_char_list)): # use _ instead as j was not being used
        sum_list = sum(two_char_list)
    result = sum_list % table_size
    return result
    


print(get_folding_hash(1234, 7))
print(get_folding_hash(12345, 11))