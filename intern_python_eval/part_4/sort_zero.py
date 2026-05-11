'''
2. Given a list of numbers,
write a program to move all zeroes to the end 
without changing the order of the other elements. 
Do not create a new list — modify in place.
'''

nums = [0, 3, 0, 5, 8, 0, 0, 2]

# Expected output: [3, 5, 8, 2, 0, 0, 0]

zero_count = nums.count(0)

i = 0

while i < len(nums):
    # print(i, len(nums))
    if nums[i] == 0:
        nums.pop(i)
    else:
        i += 1

for num in range(zero_count):
    nums.append(0)


nums = [4, -2, 7, -5, 8, -1, 3]

neg_num = []
neg_count = 0

for num in nums:
    if num < 0:
        neg_num.append(num)
        neg_count += 1


nums = [4, -2, 7, -5, 8, -1, 3]

neg_nums = []
for num in nums:
    if num < 0:
        neg_nums.append(num)

i = 0
while i < len(nums):
    if nums[i] < 0:
        nums.pop(i)
    else:
        i += 1
nums.extend(neg_nums) 

# print(nums, neg_nums)

nums = [1, 1, 2, 2, 2, 3, 4, 4, 5, 4]

i = 0

# print(len(nums)) 9
while i < len(nums) - 1:
    if nums[i] == nums[i + 1]:
        nums.pop(i + 1)
    else:
        i += 1

# print(nums)

'''
nums_1 = []

for num in nums:
    if num not in nums_1:
        nums_1.append(num)
'''

'''
nums = [1, 2, 5, 6]

for num in range(len(nums) - 1):
    if nums[num] % 2 == 0:
        nums.insert(num + 1, 0)

print(nums)
'''

nums = [1, 2, 5, 6]

i = 0

# print(len(nums)) 4

while i < len(nums):
    if nums[i] % 2 == 0:
        nums.insert(i+1, 0)
        i += 2
    else:
        i += 1

# print(nums)


nums = [1, 0, 0, 2, 3, 0, 0, 0, 4]

# [1, 0, 2, 3, 0, 4]

i = 0
# print(len(nums)) 9

while i < len(nums) - 1:
    if nums[i] == 0 and nums[i + 1] == 0:
        nums.pop(i + 1)
    else:
        i += 1

# print(nums)

nums = [1, 2, 3, 4]

# [1, 2, 2, 3, 4, 4]

i = 0
# print(len(nums)) 4

while i < len(nums):
    if nums[i] % 2 == 0:
        nums.insert(i+1, nums[i])
        i += 2
    else:
        i += 1

# print(nums)

nums = [5, 2, 2, 8, 1, 9, 3, 7]

# [5, 8, 9, 7]
# print(len(nums)) 7

count = 0

while count < len(nums):
    if nums[count] < 5:
        nums.remove(nums[count])
    else:
        count += 1

# print(nums)

nums = [2, 4, 6]

i = 0

while i < len(nums) - 1:
    add =  nums[i] + nums[i +1]
    nums.insert(i + 1, add)
    i += 2

# print(nums)

nums = [2, 7, 4, 9, 6, 1]

even_nums = []
# [7, 9, 1, 2, 4, 6]

i = 0

'''
[7, 9, 1, 2, 4, 6]
'''

while i < len(nums):
    if nums[i] % 2 == 0:
        even_nums.append(nums[i])
        nums.pop(i)

    else:
        i += 1
nums.extend(even_nums)

print(even_nums)
print(nums)

