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

def display_data(name, data, width = 30):
    #data from:
    print("Data From: '{}'".format(name))
    mean = sum(data) / len(data)
    #using format because round function misses 0.
    print("Mean Rainfall: {:.2f}".format(mean))

    display_histogram(data, width)
    # print this at the start, and the end to be dependent on the max length of stars
    equal = '=' * width
    print("{}".format(equal))

#data = read_file("sensor_a")
#print(correct_errors(data))
#display_histogram(data, 30)
data = [0, 0, 10, 15, 85, 63, 0, 23]
display_data('sensor_a', data, 40)