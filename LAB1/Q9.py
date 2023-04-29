def create_multiples_of_3(maximum):
    
    # Using list comphrension 
    multiples = [i for i in range(1, maximum) if i % 3 == 0]
    return(multiples)

    # Using loop 

    #multiples = [] 
    #for i in range (1, maximum):
        #if i % 3 = 0:
           # multiples.append(i)
    #return multiples


print(create_multiples_of_3(9))
print(create_multiples_of_3(10))
print(create_multiples_of_3(2))
print(create_multiples_of_3(33))