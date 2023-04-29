

def rate(n):
    i = 0
    total = 0
    count = 3
    while i < 20:
        j = 0
        count += 4
        while j < 2:
            total += j
            j += 1
            count += 3
        i += 1
    count += 1
    print(count)
    return total

rate(1)