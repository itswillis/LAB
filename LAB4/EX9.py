def calculate_mean(data):
    total = 0
    count = 0
    for element in data:
        try:
            total += element
            count += 1
        except TypeError:
            pass
    return total / count

print(calculate_mean([1,3,'a',4,5]))