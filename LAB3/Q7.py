def get_tuple_at(names, index):

    a_list = names[index]
    return (a_list,)

my_tuple = get_tuple_at(['May', 'Amy', 'Alan'], 1)
print(my_tuple)
print(type(my_tuple))
print(get_tuple_at(['May', 'Amy', 'Alan'], 0))