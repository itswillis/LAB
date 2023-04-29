def rate(n):
    total = 0
    i = n
    count = 2 + 1 
    while i > 0:
        j = 0
        count += 4
        while j < n:
            total += j 
            j += 2
            count += 3
        i -= 1
    count += 1
    print("Number of operations:", count)
    return total

rate(2)
rate(5)