'''
Find number that appears least
'''
nums = [5,5,5,2,2,1]

sort_list = {} 
for num in nums:
    if not num in sort_list:
        sort_list[num] = 0
        for no in nums:
            # print(no)
            if num == no:
                sort_list[num] += 1

# sort_list = {5: 3, 2: 2, 1: 1}

least_val = 0
least_key = 0
for key, val in sort_list.items():
    if val > least_val:
        least_val = val

for key, val in sort_list.items():
    if val < least_val:
        least_val = val
        least_key = key

print(least_val, least_key)