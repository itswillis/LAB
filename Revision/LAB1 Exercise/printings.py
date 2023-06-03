def print_names_and_weights(names, weights):
    print("{:10}{}".format("Name", "Weight"))
    print("-" * 16)
    for i in range(len(names)):
        print("{:10}{:.2f}".format(names[i], weights[i]))
    
print_names_and_weights(['Bill', 'Helen', 'Michael'], [76.27, 54.61, 67.92])
