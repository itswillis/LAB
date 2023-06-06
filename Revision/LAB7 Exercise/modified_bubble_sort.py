def bubble_sort(data):
    count = len(data)
    count_list = []
    swap_list = []
    for pass_num in range(len(data) - 1, 0, -1):
        count -=1  
        count_list.append(count)
        swap = 0
        for i in range(0, pass_num):
            if data[i] > data[i+1]:
                swap += 1
                data[i], data[i+1] = data[i+1], data[i]
        swap_list.append(swap)
                
    return (count_list, swap_list)

                
                


numbers = [12, 78, 81, 99, 91] # ([4, 3, 2, 1], [1, 0, 0, 0])
result = bubble_sort(numbers)
print(result)


numbers = [92, 33, 63, 6, 66, 77, 74, 51, 30, 86]
result = bubble_sort(numbers)
print(result)
