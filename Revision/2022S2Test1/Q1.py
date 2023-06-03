def is_multiple_of_3(username):
    for _ in username:
        numbers = username[-3:]
    if int(numbers) % 3 == 0:
        return True
    else:
        return False

print(is_multiple_of_3('wtan480'))
print(is_multiple_of_3('mgra734'))
print(is_multiple_of_3('dng134'))
print(is_multiple_of_3('bcar735'))