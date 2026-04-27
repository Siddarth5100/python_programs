student = {"name": "Arun", "marks": [67, 78, 90, 55]}

total = sum(student["marks"])
count = len(student["marks"])
avg = round(total / count, 2)
highest_mark = 0

for mark in student["marks"]:
    if mark > highest_mark:
        highest_mark = mark 

print(total, count, avg, highest_mark)