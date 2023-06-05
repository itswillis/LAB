def my_bubble_sort(data):
    for i in range(len(data)):
        for j in range(0, len(data) - i -1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

numbers = [76, 53, 48, 24, 12]
my_bubble_sort(numbers)
print(numbers)
