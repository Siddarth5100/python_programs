'''
Remove duplicates (keep only unique values)
'''
nums = [10,20,10,30,20,10]

# expected output = 10, 20, 30
unique_num = []

for num in nums:
    if not num in unique_num:
        unique_num.append(num)

print(unique_num)