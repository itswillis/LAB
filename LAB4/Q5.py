def sum_of_even(numbers): 

    total = 0
    for num in numbers: 
        try:
            num = int(num) # try convert into integer first
            if num % 2 == 0: 
                total += num
        except (TypeError, ValueError):
            break
    return total

my_list = [1, 2, 3, 4, -1, 2]
print(sum_of_even(my_list))

my_list = [1, 2, 3, 4, "two", 2]
print(sum_of_even(my_list))

print(sum_of_even([]))

print(sum_of_even(['NA']))