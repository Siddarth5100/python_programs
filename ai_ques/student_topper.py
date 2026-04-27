students = [
    {"name": "Arun", "marks": [80, 90, 70]},
    {"name": "Bala", "marks": [60, 75, 85]},
    {"name": "Charu", "marks": [95, 92, 88]},
    {"name": "Divya", "marks": [70, 70, 70]}
]

# expected_output => Charu

highest_total = 0
topper = ""

for student in students:
    total = 0

    for mark in student["marks"]:
        total += mark

    if total > highest_total:
        highest_total = total
        topper = student["name"]

'''
# 2nd one not efficient due to unwanted save of new dict
highest_total = 0
topper = ""
student_details = {}

for student in students:
    if student["name"] not in student_details:
        student_details[student["name"]] = 0
    
    total = 0
    for mark in student["marks"]:
        total += mark
        student_details[student["name"]] = total

    if total > highest_total:
        highest_total = total
        topper = student["name"]
    
'''

'''
# 1st code not efficient as it has extra loop
for key, value in student_details.items():
    if value > highest_total:
        highest_total = value
        topper = key
'''

print(f"Student: {topper}, Scores the highest total: {highest_total}")