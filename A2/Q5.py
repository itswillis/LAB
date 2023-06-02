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

number = 25
base = 2
print(f"{number} in base 10 is {convert_number(number,base)} in base {base}.")

number = 98
base = 8
print(f"{number} in base 10 is {convert_number(number,base)} in base {base}.")

number = 255
base = 16
print(f"{number} in base 10 is {convert_number(number,base)} in base {base}.")