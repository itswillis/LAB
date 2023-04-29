def rate(n):
    total = 0
    i = n
    count = 2 + 1
    while i > 0:
        count +=3 
        total += i
        i -= 2
    count += 1
    print(f"Number of operations: {count}")
    return total

rate(2)
rate(4)