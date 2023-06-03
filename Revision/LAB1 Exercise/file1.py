file = input("Enter a filename: ")
f = open(file, "r")
contents = f.read().split("\n") #split, when there is a new line in the file
for line in contents:
    words = line.split()
    result = ""
    for word in words:
        result += word[0]
    print(result)

f.close()
        
