def read_evens(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            result = []
            for num in data.split():
                try:
                    num = int(num)
                    if num % 2 == 0:
                        result.append(num)
                except ValueError:
                    pass
        return result
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return []


print(read_evens("eight_numbers.txt"))
'''25 -36 39
12.5

78 25
56 36'''

print(read_evens('input_unknown.txt'))
print(read_evens("with_invalid.txt"))