def read_file(sensor):

    input_file = open("{}.txt".format(sensor), "r")
    contents = input_file.read()

    list = [int(value) for value in contents.split(",")]
    input_file.close()
    return list

def correct_errors(data):
    return [value if value >= 0 else 0 for value in data]

def display_histogram(data, width=30): 
    
    scale = (width - 4) / max(data)
    for i in range(len(data)):
        # calculating the stars is multiplying each rainfall value by the scale. 
        bar = '*' * round(data[i] * scale)
        print("{:<3}|{}".format(i, bar))
