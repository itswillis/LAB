def bubble_from_end_sort(numbers):
    for i in range(len(numbers) - 1): 
        for j in range(len(numbers) - 1, i, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
        print(numbers)

data = [29, 10, 14, 37, 13]
bubble_from_end_sort(data)
print("The result is", data)