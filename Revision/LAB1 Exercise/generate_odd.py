def generate_odd_numbers(max_value):
    return [number for number in range(1, max_value+1, 2)]


a_list = generate_odd_numbers(19)
print(a_list)
