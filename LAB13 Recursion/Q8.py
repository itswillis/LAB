def get_sum(n):
    # base case
    if n == 0:
        return (0, 0)
    else:
        result = get_sum(n-1)
        sum = n + result[0]
        count = result[1] + 1 
        return (sum, count)
    
print(get_sum(3))