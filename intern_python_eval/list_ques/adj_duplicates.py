'''
Remove Adjacent Duplicates Completely

If two neighboring numbers are same,
remove BOTH.

Modify SAME list.

12mins 13:35 - 13:47
'''

nums = [1, 1, 2, 3, 3, 4, 5, 5]

# expected_output = [2, 4]

i = 0

while i < len(nums) - 1:
    if nums[i] == nums[i + 1]:
        nums.pop(i)
        nums.pop(i)
        
    else:
        i += 1 

print(nums)