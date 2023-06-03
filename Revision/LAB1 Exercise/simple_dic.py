def create_string_lengths_dictionary(fruits):
    # key: fruit
    # value: len(fruit)

    a_dict = {}

    for fruit in fruits:
        a_dict[fruit] = len(fruit)
    return a_dict
    



fruits = ['avocado', 'apple', 'blackcurrant', 'banana']
print(create_string_lengths_dictionary(fruits))
