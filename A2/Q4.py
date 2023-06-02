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

print(get_number())