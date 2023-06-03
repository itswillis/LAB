def get_first_digits(numbers):
    # must use list comprehension to create a list of first digits
    return [int(str(first)[0]) for first in numbers]

print(get_first_digits([20, 23, 16, 19, 16, 5]))
print(get_first_digits([146, 23, 1]))