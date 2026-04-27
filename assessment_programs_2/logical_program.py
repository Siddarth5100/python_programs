# ----------------------------------------que 3
'''
Given a list of numbers, write a program to move all zeroes to the end 
without changing the order of the other elements. Do not create a new list — modify in place
'''

nums = [0, 3, 0, 5, 8, 0, 2] # 0, 0, 0

# Expected output: [3, 5, 8, 2, 0, 0, 0]


count = 0
leng = len(nums)
# print(leng)
# print(count)
# print(nums)

for num in nums:
    # print(num)

    count += 1
    if num == 0:
        nums.remove(num)

for i in range(count):
    # print(i)
    nums.append(0)

# print(nums)

'''
count = 0
leng = len(nums)
# print(leng)
# print(count)
print(nums)
for num in nums:
    print(num)

    count += 1
    if num == 0:
        nums.append(num)
        nums.remove(num)
    print(nums)

print(nums)

print(count)

# for i in range(count):
#     # print(i)
#     nums.append(0)

# for i in range(len(nums), leng):
#     nums.append(0)

# print(len(nums), nums)
'''

'''
# count = 0
leng = len(nums)
# print(leng)
# print(count)

for num in nums:
    if num == 0:
        # count += 1
        nums.remove(num)
# print(count)

# for i in range(count):
#     # print(i)
#     nums.append(0)

for i in range(len(nums), leng):
    nums.append(0)

print(len(nums), nums)
'''

# for idx, val in enumerate(nums):
#     # print(idx, val)
#     if nums[idx] == 0:
#         # print(len(nums) - 1)      6
#         nums[len(nums)-1] = nums[idx]
#     else:
#         pass        

# print(nums)

'''
# type 1(praveen)
in_pos = 0
for num in nums:
    if num != 0:
        nums[in_pos] = num
        in_pos += 1

for i in range(in_pos,len(nums)):
    nums[i] = 0

print(nums)
'''

'''
# step tried (1)
for num in nums:
    print(num)
    if num == 0:
        nums.append(num)
        nums.pop(num)

print(nums)
    
[2, 0, 0, 0, 0, 0, 0]

print(dir(list))
'''

'''
# difference b/w

a = [10, 20, 30]
a.pop(1)
print(a)

a = [10, 20, 30]
a.remove(20)
print(a)
'''

# nums = [4, 7, 2, 7, 9, 5, 9]


# eg_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(6 % 2) 
# print(7 % 2)

# print("testtt", 12%2, 12%3, 12%12)
# print(4%2, 4%3, 4%4)

'''
1 2 3 5 7
if num % 2 != 0 and num % 3 != 0 and num % num == 0:
'''
# eg_prime_num = [1,2,3,5,7]

prime_num = []

for num in range(1, 11):
    if num % 2 != 0 and num % 3 != 0 and num % num == 0:
        # print(num)
        pass


# print(12 % 3, 12 % 2, 12 % 12)
# print()
# print(12 / 3, 12 / 2, 12 / 12)
# print()
# print(11 % 3, 11 % 2, 11 % 11)
# print()
# print(11 / 3, 11 / 2, 11 / 11)
# print()
# print(15 / 3, 15 / 2, 15 / 15)
# print(15 % 3, 15 % 2, 15 % 15)




# num % 3 == 0
# num % num == 0

for num in range(1, 11):
    print(num)
    if num % 2 == 0:
        print("True")
    else:
        print("False")


num = 7
count = 0

for no in range(num):
    count += 1
    no % 2

print(count)  