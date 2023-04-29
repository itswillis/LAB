def binary_search(names_list, target_name): 
    names_list.sort()
    # algorithm
    left_index = 0 
    right_index = len(names_list) -1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        guess = names_list[mid_index]
        print(f'left: {left_index}, mid: {mid_index}, right: {right_index}')
        
        if guess == target_name: 
            return True
        elif guess < target_name:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    
    return False

my_list = ["Andrew", "Benjamin", "Catherine", "David", "Elizabeth", "Frances", "Gabriel", "Hannah", "Isaac", "Julia", "Kevin", "Laura", "Michael", "Natalie", "Olivia", "Patrick"] 
print(binary_search(my_list, "Hannah"))

my_list = ["Hannah", "Isaac", "Julia", "Kevin", "Laura", "Michael", "Natalie"]
print(binary_search(my_list , "King"))
