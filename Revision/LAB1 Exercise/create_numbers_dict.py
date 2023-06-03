def create_numbers_dict(max_value):
    # 0, max_value, 2

    numbers = []
    for i in range(0, max_value, 2):
        numbers.append(i)

    return {num: num**2 for num in numbers}

print(create_numbers_dict(5))
