nums = [4, 9, 2, 7, 1, 8]

'''
1, 2, 4, 8, 9
'''
asc_num = sorted(nums)
desc_num = sorted(nums, reverse=True)

'''
for num in range(len(nums)):
    # print(nums[num])
    for no in range(len(nums) - 1):
        # print(no + 1)
        if nums[num] < nums[no]:
            pass 
'''
       

# print(asc_num, desc_num)

'''
a = 10
b = 20

print(a, id(a))
print(b, id(b))

a, b = b, a

print(a, id(a))
print(b, id(b))
'''

a = 5
b = 10

a, b = b, a

nums = [1, 2, 3, 4]

nums[0], nums[-1] = nums[-1], nums[0]

nums = [10, 20, 30, 40]

nums[1], nums[2] = nums[2], nums[1]

a = 15
b = 10

# if a > b:
#     print(a)
# else:
#     print(b)

# nums = [5, 2, 8, 1]

# for i in range(len(nums) - 1):
#     print(nums[i], nums[i+1])
'''
nums = [5, 3]

for num in range(len(nums) - 1):
    if nums[num] > nums[num + 1]: # how to manage the index out of range error?
        print("swap needed")
        
nums = [5, 2, 8, 1]

for num in range(len(nums) - 1):
    print(nums[num], nums[num + 1]) # how to manage the index out of range error?
'''
 
nums = [10, 20, 30]

for num in range(len(nums)):
    # print(num)
    pass

# for idx, val in enumerate(nums):
#     print(idx)

for num in range(len(nums) - 1):
    # print(nums[num], nums[num+1])
    pass

# for i in range(len(nums)):
#     print(nums[i], nums[i+1])

nums = [5, 2, 8, 1]

for num in range(len(nums) - 1):
    # print(num)
    if nums[num] > nums[num + 1]:
        nums[num], nums[num + 1] = nums[num + 1], nums[num]
    
# print(nums)

