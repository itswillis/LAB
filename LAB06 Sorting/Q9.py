def bubble_single_pass(data, index):
        for i in range(index):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i] #data j is not data[j+1] while data[j+1] is now data[j]



def my_bubble_sort(data): 
        for index in range(len(data) - 1, 0, -1):
            bubble_single_pass(data, index)

numbers = [76, 53, 48, 24, 12]
my_bubble_sort(numbers)
print(numbers)