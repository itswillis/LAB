def is_mirror(numbers, start, end):
    # base case 
    if start == end or end < start: 
        return True
    # recursive case
    return numbers[start] == numbers[end] and is_mirror(numbers, start + 1, end - 1)

e = [1, 2, 3, 4, 2, 1]
print(is_mirror(e, 0, len(e) - 1))