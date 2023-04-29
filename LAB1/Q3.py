def remove_multiples_of_3(numbers):
    i = len(numbers) - 1
    while i >= 0:
        if numbers [i] % 3 == 0:
            numbers.pop(i)
        # iterate backwards everytime, without using reversed() which gives an error
        i -= 1
    return numbers


values = [5, 3, 1, 2, 3]
remove_multiples_of_3(values)
print(values)

values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
remove_multiples_of_3(values)
print(values)