'''
Find:
total for each student
topper
subject-wise highest scorer
'''

students = [
    {"name": "Arun", "marks": {"Math": 78, "Science": 82, "English": 74}},
    {"name": "Bala", "marks": {"Math": 88, "Science": 76, "English": 90}},
    {"name": "Charu", "marks": {"Math": 91, "Science": 89, "English": 93}}
]

'''
total : 78 + 82 + 74 = 234, 254, 273
topper : bala
sub : math 91 sci 89 eng 93
'''

total = {}
topper = ""
subwise = {}

for student in students:
    if student["name"] not in total:
        total[student["name"]] = {"total_marks": 0}

    total_mark = 0
    for mark in student["marks"]:
        total_mark += student["marks"][mark]
        total[student["name"]]["total_marks"] = total_mark

highest_total = 0
for key, value in total.items():
    if value["total_marks"] > highest_total:
        topper = key
