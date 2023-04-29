def read_file(sensor):

    input_file = open("{}.txt".format(sensor), "r")
    contents = input_file.read()

    list = [int(value) for value in contents.split(",")]
    input_file.close()
    return list


print(read_file("sensor_a")) 

