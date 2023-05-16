def get_pair_sum(numbers): 
    sums_list = []
    try:
        for i in range(0, len(numbers)-1):
            sum = float(numbers[i]) + float(numbers [i+1])
            sums_list.append(sum)
    except (TypeError, ValueError):
        sums_list.append(0)
    return sums_list



print(get_pair_sum([1.5, 2, 3, 4]))