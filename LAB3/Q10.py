def append_number_string_to(number_string, numbers_list=[]):
    if numbers_list == []:
        numbers_list = [number_string]
    else: 
        numbers_list.append(number_string)
    return numbers_list


my_list = append_number_string_to('one')
print(my_list)
my_list = append_number_string_to('two')
print(my_list)

my_list = append_number_string_to('We Own It')
print(my_list)
my_list = append_number_string_to('See You Again', my_list)
print(my_list)
my_list = append_number_string_to('Gangnam Style')
print(my_list)

my_list = []
my_list = append_number_string_to('Gangnam Style', my_list )
print(my_list)