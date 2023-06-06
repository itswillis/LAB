def  binary_search(names_list, target_name):

    left = 0
    right = len(names_list) - 1

    while left <= right:
        mid = (left+right)//2
        mid_value = names_list[mid]
        if mid_value == target_name:
            print(f"left: {left}, mid: {mid}, right: {right}")
            return True
        elif mid_value < target_name:
            print(f"left: {left}, mid: {mid}, right: {right}")
            left = mid + 1
        else:
            print(f"left: {left}, mid: {mid}, right: {right}")
            right = mid - 1
    return False

my_list = ["Andrew", "Benjamin", "Catherine", "David", "Elizabeth", "Frances", "Gabriel", "Hannah", "Isaac", "Julia", "Kevin", "Laura", "Michael", "Natalie", "Olivia", "Patrick"] 
print(binary_search(my_list, "Hannah"))

my_list = ["Hannah", "Isaac", "Julia", "Kevin", "Laura", "Michael", "Natalie"]
print(binary_search(my_list , "King"))
