nums = [0, 1, 2, 2, 3, 0, 4, 2]

val = 2

# for idx, num in enumerate(nums):
#     print(idx, num)


for num in range(len(nums)):
    # print(num, nums[num])
    if nums[num] == val:
        # print(num, nums[num])

        pass

# nums = [1, 2, 3, 4, 5, 6, 7]

# nums.sort(reverse=True)

# print(nums)

num_1 = [9, 2, 6, 1, 5, 7]
num_2 = []
# print(len(num_1))

for no in range(len(num_1)-1, -1, -1):
    # print(num_1[no])
    # print(no, num_1[no])
    # num_2.append(num_1[no])
    num_1.append(num_1[no])

print(num_1)
print(num_2)