def create_baby_names_dictionary(names_list): 
    dic = {} 
    names_list = sorted(names_list)
    for name in names_list: 
        letter = name[0]
        if letter not in dic:
            dic[letter] = [name] 
        else: 
            dic[letter].append(name)
    return dic

#test
names = ['Alex', 'Bob', 'Connor', 'Daniel', 'Asher', 'Anthony', 'Benjamin']
baby_names_dictionary = create_baby_names_dictionary(names)
for key in sorted(baby_names_dictionary ):
    print(key, baby_names_dictionary [key])