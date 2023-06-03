def twoSum(nums, target):
    a = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if ((nums[i] + nums[j]) == target):
                a.append(i)
                a.append(j)
                break
            else:
                continue
    return a 

values = [0,0,1,2,3,4]
value = 6 
print(twoSum(values, value))