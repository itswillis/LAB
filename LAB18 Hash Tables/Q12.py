def hash_quadratic(key, table):
    probe = 1 
    num = 1
    size = len(table)
    index = key % len(table)

    while table[index] is not None:
        probe += 1
        index = (key + num**2) % size
        num += 1
    
    table[index] = key
    return probe


values = [88, None, 35, 25, None, None, None, None, 10, None, 32]
probes = hash_quadratic(11, values)
print('Table =', values)
print('Probes =', probes)