'''
Your program should:

calculate total + average per student
assign grades:
avg >= 90 → A
avg >= 75 → B
avg >= 50 → C
else → Fail
find topper
print failed students
create final summary dictionary

Arun -> Total: 250, Avg: 83.33, Grade: B
'''

marks = {
    "Arun": [78, 82, 90],
    "Bala": [88, 76, 95],
    "Charu": [91, 89, 84],
    "Deepa": [45, 55, 60]
}

student_details = {}
topper = ""
top_mark = 0
failed_student = []

for student in marks:
    if student not in student_details:
        student_details[student] = {"total": 0}
    
    for mark in marks[student]:
        student_details[student]["total"] += mark

    avg = student_details[student]["total"] / len(marks[student])
    student_details[student]["avg"] = round(avg, 2)

for avg in student_details:
    if student_details[avg]["avg"] >= 90:
        student_details[avg]["grade"] = "A"

    elif student_details[avg]["avg"] >= 75:
        student_details[avg]["grade"] = "B"

    elif student_details[avg]["avg"] >= 50:
        student_details[avg]["grade"] = "C"

    else:
        student_details[avg]["grade"] = "Fail"    

    if student_details[avg]["total"] > top_mark:
        top_mark = student_details[avg]["total"]
        topper = avg

    if student_details[avg]["grade"] == "Fail":
        failed_student.append(avg)
    
# print(student_details)
# print(topper, top_mark)

print(f"Topper: {topper}, Top Mark: {top_mark}, Avg: {student_details[topper]["avg"]}, Grade: {student_details[topper]["grade"]}")