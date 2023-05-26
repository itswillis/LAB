def hash_double(key, table):
    probe = 1 
    size = len(table)
    index = key % len(table)

    while table[index] is not None:
        probe += 1
        index = index + 5 - (key % 5) % size
    
    table[index] = key
    return probe



values = [88, None, 35, 25, 10, None, None, None, None, None, 32]
probes = hash_double(11, values)
print('Table =', values)
print('Probes =', probes)