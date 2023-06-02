'''def get_selection(start, end):
        value = input("Please make a selection: ")
        try: 
            value = int(value)
            if int(value) >= start and int(value) <= end:
              return value
        except ValueError:
             False
        while True: 
            value = input("Invalid selection. Try again: ")
            try:
                value = int(value)
                if int(value) >= start and int(value) <= end:
                      return value
            except ValueError:
                  False

# SIMPLIER AND MORE EFFICIENT
'''

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




print(get_selection(0, 5))