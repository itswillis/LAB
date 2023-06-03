def two_sum(nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]
    

nums = [3,2,5]
target = 7

print(two_sum(nums, target))
