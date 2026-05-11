'''
Rotate List Left by One Position

Move first element to end

Modify SAME list

expected_out = [2, 3, 4, 5, 1]
'''

nums = [1, 2, 3, 4, 5]


first_val = nums[0]
nums.pop(0)
nums.append(first_val)

print((nums))

'''
for num in range(len(nums)):
    first_val = nums[num]
    nums.remove(nums[num])
    nums.append(first_val)
    break

print(nums)
'''

'''
num_1 = []

for num in nums:
    num_1.append(num)
    nums.remove(num)
    break

nums.extend(num_1)
'''