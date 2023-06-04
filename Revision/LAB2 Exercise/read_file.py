def read_file(sensor):
    filename = open(f'{sensor}.txt', 'r')
    f = filename.read().split(',')

    a = []
    for contents in f:
        contents = int(contents)
        a.append(contents)

    return a

        
print(read_file('sensor_a'))
    
