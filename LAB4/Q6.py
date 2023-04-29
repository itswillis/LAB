def sum_of_even_continue(numbers): 

    total = 0
    for num in numbers: 
        try:
            num = int(num) # try convert into integer first
            if num % 2 == 0: 
                total += num
        except (TypeError, ValueError):
            pass
    return total


my_list = [1, 2, 3, 4, -1, 2]
print(sum_of_even_continue(my_list))
print(sum_of_even_continue([-1, 0, 10, 20, 'ten', 35, 45, 105, 20]))
my_list = [1, 2, 3, 4, "two", 2]
print(sum_of_even_continue(my_list))
print(sum_of_even_continue([]))