# return the two sums that make up target:

def twoSum(nums, target):
    a = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if ((nums[i] + nums[j]) == target):
                a.append(nums[i])
                a.append(nums[j])
                break
            else:
                continue
    return a 


values = [2,7,11,15]
value = 9
print(twoSum(values, value))