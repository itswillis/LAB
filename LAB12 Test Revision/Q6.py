def is_multiple_of_3(username):
    digits = username[-3:]
    return int(digits) % 3 == 0

print(is_multiple_of_3('wtan480'))
print(is_multiple_of_3('mgra734'))
print(is_multiple_of_3('dng134'))
print(is_multiple_of_3('bcar735'))