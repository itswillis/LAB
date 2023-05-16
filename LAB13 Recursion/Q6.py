# Write a recursive function that takes a Python list of numbers and returns a NEW list containing only the even numbers 
# which are greater than 0 (in  the same order as the original list)

# Function should return an empty list if there are no positive and even numbers in the parameter list 

def get_positive_even_list(numbers):
    empty_list = []
    # base case
    if not numbers:
        return []
    # recursive case
    else:
        if numbers[0] % 2 == 0:
            if numbers[0] > 0:
                empty_list.append(numbers[0])
        return (empty_list + get_positive_even_list(numbers[1:]))

print("{}".format(get_positive_even_list([2, 3, -5, -6, 8, 5, 9, 10])))
print("{}".format(get_positive_even_list([-1, 0, 1])))