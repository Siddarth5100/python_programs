'''
Without using count():

Find duplicate numbers
Find most repeated number
Remove duplicates
Find second highest number

Expected output idea:

Duplicates: [4, 7]
Most repeated: 7
Unique: [4, 7, 2, 9, 1]
Second highest: 7
'''

nums = [4, 7, 2, 7, 9, 4, 1, 7]

duplicate_nos = []
num_count = {}
most_repeated_num = 0

# Find duplicate numbers
for num in nums:
    if num not in num_count:
        num_count[num] = 0
    num_count[num] += 1

count = 0
for key, val in num_count.items():
    if val > 1:
        duplicate_nos.append(key)
    
    # Find most repeated number
    if val > count:
        count = val
        most_repeated_num = key

# Remove duplicates
sort_num = set(nums)

# Find second highest number
first_high = max(nums)
sec_high = 0

for num in nums:
    if num > sec_high and num != first_high:
        sec_high = num

# print(duplicate_nos)
# print(most_repeated_num)
# print(sort_num)
# print(first_high)
# print(sec_high)