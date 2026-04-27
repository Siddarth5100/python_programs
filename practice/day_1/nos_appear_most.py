'''
Given a list of numbers,
find the number that appears the most.
'''

nums = [1, 2, 2, 3, 3, 3, 4]

# Expected output: 3

sorted_nums = {}

for no in nums:
    if not no in sorted_nums:
        sorted_nums[no] = 0
        for num in nums:
            if no == num:
                sorted_nums[no] += 1

# {1: 1, 2: 2, 3: 3, 4: 1}

highest_no_count = 0
numb = 0

for key, value in sorted_nums.items():
    if value > highest_no_count:
        highest_no_count = value
        numb = key

print(sorted_nums)
print(f"Number {highest_no_count}, has the highest_count : {numb}")