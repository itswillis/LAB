def triangular_number(n):
    # base case: 
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    elif n == 2: 
        return 3
    
    # recursion case: 
    else:
        return ((3*triangular_number(n-1) - (3*triangular_number(n-2)) + triangular_number(n-3)))
    
print(triangular_number(4))