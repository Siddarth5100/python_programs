'''
Remove Numbers Between 10 and 20

expected_out = [5, 25, 7, 30]
'''

nums = [5, 12, 18, 25, 7, 15, 30]

i = 0

while i < len(nums):
    if nums[i] >= 10 and nums[i] <= 20:
        nums.pop(i)
    else:
        i += 1

print(nums)