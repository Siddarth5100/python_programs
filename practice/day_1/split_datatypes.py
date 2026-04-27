data = [10, "Pen", 20, "Book", 30, "Bag", 40]

strings = []
nums = []

for d in data:
    if type(d) == int:
        nums.append(d)
    else:
        strings.append(d)

print(strings, nums)

'''
we can use isinstances
'''
