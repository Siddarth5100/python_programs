'''
Tasks:

Find total marks of each student
Find average of each student
Print topper name
Print subject-wise highest mark
'''

students = {
    "Arun": [78, 82, 90],
    "Bala": [88, 76, 95],
    "Charu": [91, 89, 84]
}

total_marks = {} # will this data type works? how to manage if the student has the same name
topper = ""

for student in students:
    total = 0
    count = 0
    for mark in students[student]: # inside we have list so we want this loop
        total += mark
        count += 1
        
    total_marks[student] = {"total": total}
    total_marks[student]["avg"] = round(total / count, 2)
    # print(students[student])
        

highest_total = 0
for total in total_marks:
    if total_marks[total]["total"] > highest_total:
        highest_total = total_marks[total]["total"]
        topper = total
