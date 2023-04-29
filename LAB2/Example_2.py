def read_file(sensor):

    input_file = open("{}.txt".format(sensor), "r")
    contents = input_file.read()

    list = [int(value) for value in contents.split(",")]
    input_file.close()
    return list

def correct_errors(data):
    return [value if value >= 0 else 0 for value in data]


data = read_file("sensor_a")
print(correct_errors(data))