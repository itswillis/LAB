def calculate_mean(data):
    try:
        total = sum(data)
        mean = total / len(data)
        return mean
    except TypeError: 
        return ("Error: Invalid number found!")



print(calculate_mean([1,3,'a',4,5]))