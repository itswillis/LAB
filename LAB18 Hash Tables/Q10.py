def hash_linear(key, table):
    probe = 1 
    size = len(table)
    index = key % len(table)

    while table[index] is not None:
        probe += 1
        index = (index + 1) % size
    
    table[index] = key
    return probe



values = [88, 10, 35, 25, None, None, None, None, None, None, 32]
result = hash_linear(11, values)
print('Table =', values)
print('Probes =', result)

values = [None, None, 2, 3, 4, 11, 18]
result = hash_linear(9, values)
print('Table =', values)
print('Probes =', result)