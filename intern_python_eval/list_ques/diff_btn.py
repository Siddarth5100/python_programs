'''
Insert Difference Between Neighbors

Insert absolute difference between adjacent numbers.
'''

nums = [10, 7, 15]

'''
expected_out = [10, 3, 7, 8, 15]

|10 - 7| = 3
|7 - 15| = 8
'''

i = 0

while i < len(nums) - 1:
    total = abs(nums[i] - nums[i + 1])
    nums.insert(i+1, total)
    i += 2

print(nums)