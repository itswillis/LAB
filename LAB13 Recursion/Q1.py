# Write a recursive function (base case and recursion) which takes in two parameters start, stop, and prints out the 
# numbers from start to stop, followed by the text "Go"

def count_down(start, stop): 
    if start < stop: 
        print("Go!")
    else:
        print(start)
        count_down(start-1, stop)

count_down(6, 3)