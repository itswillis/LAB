'''
Define a function named get_valid_dice() for a "Dice simulation" game. The function reads input from the user until the value 
they enter is a valid value (i.e. 1 to 6 inclusive). The function then returns the value.

Use a try ... except block to handle any exceptions that might occur.

If the user enters an invalid value (i.e. a value that is outside the range 1 - 6 (inclusive) or a value which generates a 
TypeError or a ValueError) then the function should continue to ask the user to enter an input until the value they enter is valid.

'''


def get_valid_dice(): 

    while True:
        try:
            dice = int(input("Enter a valid dice: "))
            if 1 <= dice <= 6: 
                return dice
        except (TypeError, ValueError): 
            pass
    
value = get_valid_dice()
print('Valid input:', value)