"""
Write a function get_cube_volume(length) which takes the length of a cube as a parameter, and returns the volume of the cube rounded 
to the nearest integer. The formula for the volume of a cube is:

length^3

"""




def get_cube_volume(length): 
    # Initialise error
    Error = ""


    try: 
        length = float(length)
        volume = length**3
        if length == 0:
            Error = "ERROR: Not a cube!"
            volume = 0 
        elif length < 0:
            Error = "ERROR: Length must be positive!"
            volume = 0 
    except TypeError: 
        Error = "ERROR: The type is incorrect!"
        volume = 0 
    except ValueError: 
        Error = "ERROR: The value is invalid!"
        volume = 0 

    return (round(volume), Error)


print(get_cube_volume(10.5)) 
print(get_cube_volume(-1))
print(get_cube_volume(0))
print(get_cube_volume('ten'))
print(get_cube_volume([1,2,3]))