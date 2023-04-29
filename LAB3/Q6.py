def no_negatives(numbers):
    #check if the list is empty
    if numbers == []: 
        return True
    
    # the problem with this is it checks for the first number only, it doesnt finish iterating through the list. 
    # this is because we are returning so early which finishes the loop
    for number in numbers:
        if number < 0:
            negative = 1 
            # the problem with this is it keeps looping and updating the last value, need to break as soon as it finds the negative
            break
        else:
            negative = 0
    
    return False if negative == 1 else True

print(no_negatives([-5, -1, 3, 4]))
print(no_negatives([1, 2, 3]))
print(no_negatives([1, 2, -3]))

numbers = []
print(no_negatives(numbers))

numbers = [-3]
print(no_negatives(numbers))