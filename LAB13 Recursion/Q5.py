# This function calculates and returns the SUM of all multiples of m in the list
# The function should return 0 if the parameter is an empty list or there are no multiples of m in the list.
def get_sum_multiples(numbers, m):
    # base case:
    if not numbers:
        return 0
    elif numbers[0] % m == 0:
        return numbers[0] + get_sum_multiples(numbers[1:], m)
    else:
        return get_sum_multiples(numbers[1:], m)

numbers = [1, 4, 5, 9, 11]
print(get_sum_multiples(numbers, 3))