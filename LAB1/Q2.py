#A factory requires a program to calculate the number of containers needed to store a given number of items. 
#Each container can fit up to 10 items.
items = int(input("Enter the number of items: "))
if (items > 10 and items % 10 != 0): 
    container = (items/10) + 1
    print("You need {} containers for {} items." .format(int(container), items))
elif items == 1: 
    container = 1
    print("You need {} container for {} item." .format(int(container), items))
elif items <= 0: 
    print("Invalid number!")
elif (items <= 10): 
    container = 1
    print("You need {} container for {} items." .format(int(container), items))
else: 
    container = items/10 
    print("You need {} containers for {} items." .format(int(container), items))






