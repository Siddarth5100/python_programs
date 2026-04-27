nums = [0, 3, 0, 5, 8, 0, 2]

'''
[3, 5, 8, 2]
[3, 5, 8, 2, 0, 0, 0]
'''
count = 0
for num in nums:
    if num == 0:
        count += 1
        nums.remove(num)
        nums.append(0 * count)

# print(nums, count)

list_1 = [1, 2, 4]
list_2 = [1, 3, 4]

# print(list_1)
# print(list_2)
# list_1.extend(list_2)
# print(list_1)

for num in list_2:
    # print(num)
    list_1.append(num)

# [1, 2, 4, 1, 3, 4]
'''
# 1     2 4 1 3 4
# 124134
'''

# [1, 1, 2, 3, 4, 4]
for no in range(len(list_1)):
    # print(list_1[no], no)
    for num in range(len(list_1)-1, -1, -1):
        # if list_1[no] >
        pass

