def rate(n):
    i = 1
    total = 0 
    count = 3
    while i < n:
        count += 3
        total += i 
        i *= 1 
    count += 1
    print(count)
    return total 

rate(5)
rate(10)
