def read_sum_odds(filename): 
    input_file = open(filename, 'r')
    contents = input_file.readlines()

    result = [] 

    for line in contents: 
        nums = line.split()
        sum_odds = 0 
        for num in nums: 
            if int(num) % 2 != 0: 
                sum_odds += int(num)
        result.append(sum_odds)
    input_file.close() 

    return result




filename = "Lab07Q03_1.txt"
print(read_sum_odds(filename))