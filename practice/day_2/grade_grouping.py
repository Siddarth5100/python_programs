'''
Group student names by grade.
'''

students = [
    {"name": "Akash", "grade": "A"},
    {"name": "Bala", "grade": "B"},
    {"name": "Chandru", "grade": "A"},
    {"name": "Divya", "grade": "B"},
    {"name": "Farhan", "grade": "C"}
]

student_group = {}

for student in students:
    if student["grade"] not in student_group:
        student_group[student["grade"]] = []

    student_group[student["grade"]].append(student["name"])

print(student_group)