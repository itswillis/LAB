def  display_menu():
    print("*****************************")
    print("New Zealand Births Statistics")
    print("1. Births by Region")
    print("2. Births by Year")
    print("0. Save and Exit")
    print("*****************************")

def get_user_option_input(): 
        number = ""
        while number not in ('0', '1', '2'):
            number = (input("Enter selection: "))
        return number

number = get_user_option_input()
print(number)
