def bubble_sort(data):
    compare = [] 
    swap = [] 
    for pass_num in range(len(data) - 1, 0, -1):
        compare.append(pass_num)
        count = 0 # reset count
        for i in range(0, pass_num):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                count += 1  

        swap.append(count)

    return(compare, swap)


numbers = [12, 78, 81, 99, 91]
result = bubble_sort(numbers)
print(result)

numbers = [92, 33, 63, 6, 66, 77, 74, 51, 30, 86]
result = bubble_sort(numbers)
print(result)