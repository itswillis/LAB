def ternary_search(num_list, value):
    print("Number List:", num_list)
    n = len(num_list)

    if n == 0:
        return False

    midpoint1 = n // 3
    midpoint2 = 2 * midpoint1

    if num_list[midpoint1] == value or num_list[midpoint2] == value:
        return True
    elif value < num_list[midpoint1]:
        return ternary_search(num_list[:midpoint1], value)
    elif value > num_list[midpoint2]:
        return ternary_search(num_list[midpoint2 + 1:], value)
    else:
        return ternary_search(num_list[midpoint1 + 1:midpoint2], value)

num_list = [1, 2, 3]
for i in range(0, 5):
    print(f"The number {i} is in the list {num_list}: {ternary_search(num_list, i)}")
