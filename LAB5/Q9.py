def rate(n):
    total = 0
    i = 1
    count = 3
    while i < n:
        j = n
        count += 4
        while j > 0:
            total += j 
            j -= 1
            count += 3
        i *= 2
    count += 1
    print("Number of operations:", count)
    return total

rate(2)
rate(4)