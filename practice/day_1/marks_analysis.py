marks = [0, 45, 67, 89, 23, 67, 90, 45]

highest_mark = 0
lowest_mark = marks[0]
total = 0
average = 0

count = 0

for mark in marks:
    total += mark
    count += 1
    if mark > highest_mark:
        highest_mark = mark
    
    if mark < lowest_mark:
        lowest_mark = mark

average = round(total / count, 2)

print(highest_mark, lowest_mark, total, average)