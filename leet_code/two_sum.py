nums = [2, 7, 11, 15]
target = 9

# output = [0, 1]

def two_sum():
    for i in range(len(nums)):
    # print(i, nums[i])
        for j in range(i + 1, len(nums)):
            # print(nums[i])
            # print(nums[j])
            if nums[i] + nums[j] == target:
                # print(i, j)
                return [i, j]
            
print(two_sum())
        
        