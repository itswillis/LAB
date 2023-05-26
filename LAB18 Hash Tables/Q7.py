def get_simple_numeric_hash(key, table_size):
    square = str(key ** 2) 
    removed_square = square[1:len(square)-1]
    result = int(removed_square) % table_size
    return result

print(get_simple_numeric_hash(655, 13))
print(get_simple_numeric_hash(654, 13))
print(get_simple_numeric_hash(653, 13))

print(get_simple_numeric_hash(1000, 19))
print(get_simple_numeric_hash(1001, 19))
print(get_simple_numeric_hash(1002, 19))