def bubble_single_pass(data, index):
        for i in range(index):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i] #data j is not data[j+1] while data[j+1] is now data[j]

numbers = [76, 53, 48, 24, 12]
bubble_single_pass(numbers, 4)
print(numbers)

	
numbers = [76, 53, 48, 24, 12]
bubble_single_pass(numbers, 3)
print(numbers)

numbers = [76, 53, 48, 24, 12]
bubble_single_pass(numbers, 2)
print(numbers)

numbers = [76, 53, 48, 24, 12]
bubble_single_pass(numbers, 1)
print(numbers)

numbers = [92, 33, 63, 6, 66, 77, 74, 51, 30, 86]
bubble_single_pass(numbers, 4)
print(numbers)