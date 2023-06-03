# should return the two sum that make up the target and their indexes

def twoSum(nums, target):
    a = []
    b = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if ((nums[i]+nums[j])==target):
                a.append(nums[i])
                a.append(nums[j])
                b.append(i)
                b.append(j)
                break
            else:
                continue
    return a, b



values = [2,7,11,15] # return ([2,7], [0,1])
value = 9
print(twoSum(values, value))