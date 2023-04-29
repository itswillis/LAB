def read_english_spanish_info(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split("\n")
    
    info = [] 

    for language in contents: 
        words = language.split(":")
        group = (words[-1], words[0])
        info.append(group)
    input_file.close()
    return info

print(read_english_spanish_info('english_to_spanish1.rtf'))