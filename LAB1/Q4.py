# Add GST to prices passed through list
def apply_gst(prices_list): 
    for i in range (len(prices_list)): 
        prices_list[i] = prices_list[i] * (1 + (15/100))
    

# test
prices = [1.59, 45.67, 3.56, 7.29, 8.36, 1034.99]
apply_gst(prices)
print(', '.join(["{:.2f}".format(price) for price in prices]))