def display_intro():
    print("**********************************************")
    print("**        A Number Converter Program        **")
    print("** Decimal --> Binary, Octal or Hexadecimal **")
    print("**********************************************")

def display_menu():
    print("1. Convert to binary value")
    print("2. Convert to octal value")
    print("3. Convert to hexadecimal value")
    print("4. Quit the program")

def get_selection(start, end):
    value = input("Please make a selection: ")
    while True:
        try:
            value = int(value)
            if value >= start and value <= end:
                return value
        except ValueError:
            pass
        value = input("Invalid selection. Try again: ")

def get_number():
    value = input("Please enter a positive integer: ")
    while True:
        try: 
            value = int(value)
            if value > 0: 
                return value
        except ValueError:
            pass
        value = input("Invalid entry. Try again: ")

def convert_number(number, base):
    # base case: 
    if number == 0:
        return ""
    # recursive case: 
    algorithm = number // base 
    converted = (number % base)

    if converted > 9:
        a_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'} 
        converted = a_dict[converted]
    else:
        converted = str(converted)
    return convert_number(algorithm, base) + converted

def main():
    display_intro()
    display_menu()
    print('')
    selection = get_selection(1, 4)

    while selection != 4: 
        if selection == 1:
            value = get_number()
            converted_number = convert_number(value, 2) # binary in base 2
            print(f"{value} is {converted_number} in binary")
            print('')
    
        elif selection == 2: 
            value = get_number()
            converted_number = convert_number(value, 8) # octal in base 8
            print(f"{value} is {converted_number} in octal")
            print('')

        elif selection == 3:
            value = get_number()
            converted_number = convert_number(value, 16) # hexadecimal in base 16 
            print(f"{value} is {converted_number} in hexadecimal")
            print('')

        # re-display menu after conversion
        display_menu()
        print('')
        selection = get_selection(1, 4)

main()