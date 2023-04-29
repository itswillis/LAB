my_dict = {'test1':1,'test2':2}
key = input('Enter a key: ')
try:
    print(my_dict[key])
except: 
    print("ERROR: Invalid Key!")