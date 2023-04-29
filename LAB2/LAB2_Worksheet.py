def enter_number(): 
    first = int(input("Enter an integer: "))
    second = int(input("Enter an integer: "))
    while (first < 0 or second < 0):
        print("You must enter two positive integers!")
    return first, second

def first_and_second(first, second):   
    if first > second: 
        for number in range(second, first + 1):
            print(number, end = " ") 
    print()
    try_again()

def try_again(): 
    test = int(input("Do you want to try again using new integers? Enter 1 for Yes and 2 for No: "))
    if test == 1: 
        first, second = enter_number()
        first_and_second(first, second)
        #run the function again  
        # end the function 
    else: 
        exit()

first, second = enter_number()
first_and_second(first, second)