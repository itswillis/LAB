""" 
Flight attendants may need to pass a lift and reach test, which usually requires flight attendants to be at least 160 
centimetres tall, and able to lift heavy bags and emergency equipment. 
We need to determine whether a person is eligible to apply to be a flight attendant. 
The minimum height requirement is 160.
"""

def is_eligible(height_value): 
    # any type parameter
    # first try convert the height into an integer
    # if it is an integer, float or string that represents an integer, conversion is successful
    # otherwise: this will generate TypeError ( if the type can not be convereted into an integer) or 
    # ValueError if the type is valid but the value cannot be converted into an integer

    # function should return a tuple (first item, should be a boolean of whether or not the height is valid, the second 
    # message should be the height or error message)

    Eligible = False

    try: 
        height = int(height_value)
        if height < 160: 
            Eligible = False
        else: 
            Eligible = True
    except TypeError: 
        height = ("ERROR: The type is incorrect!")
    except ValueError:
        height = ("ERROR: The value is invalid!")

    return (Eligible, height)

data = is_eligible('160')
print(data)
print(type(data))
print(is_eligible('abc'))
print(is_eligible([1, 2, 3]))
print(is_eligible('153'))