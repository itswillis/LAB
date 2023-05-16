# Write a recursive function (base case and recursion) which takes in two parameters start, stop, and prints out the 
# numbers from start to stop, followed by the text "Go"

def count_down(start, stop): 
    if start > stop:    # base case
        print("Go!") 
    else:         # recursive case (start + 1)
        print(start)
        count_down(start + 1, stop)



count_down(1, 5)

# 1
# 2
# 3
# 4
# 5
# Go!