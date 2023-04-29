def read_data(filename): 
    file = open(filename, "r")
    contents = file.read().splitlines()

    result = [] 
    for line in contents: 
        fields = line.strip().split("\t")
        year = int(fields[0])
        region = fields[1]
        births = int(fields[2])
        result.append((year, region, births))
    file.close()
    return result

data = read_data("birth1.txt")
print(data)
print(type(data))
print(type(data[0]))
print(type(data[0][0]), type(data[0][1]), type(data[0][2]))

