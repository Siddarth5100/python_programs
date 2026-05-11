'''
Merge Consecutive Equal Numbers

If neighboring numbers are same:

merge them into their SUM
continue checking again

Modify SAME list

expected out = [4, 3, 4, 4, 4, 5]
'''

nums = [2, 2, 3, 4, 4, 4, 5]

i = 0

while i < len(nums) - 1:
    if nums[i] == nums[i + 1]:
        total = nums[i] + nums[i + 1]
        nums[i] = total
        nums.pop(i + 1)    
    else:
        i += 1

print(nums)