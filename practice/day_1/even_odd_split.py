nums = [12, 5, 8, 21, 30, 7, 18]

eve_no = []
odd_no = []

for num in nums:
    if num % 2 == 0:
        eve_no.append(num)
    else:
        odd_no.append(num)

print(eve_no)
print(odd_no)

'''
# what will happen if i do like this?
for num in nums:
    if num % 2 == 0:
        eve_no.append(num)
    odd_no.append(num)
'''
