seats = [1, 2, 3, 5, 6, 8, 9, 10]

missing_num = []
for num in range(1, 11):
    if num not in seats:
        missing_num.append(num)

print(missing_num)