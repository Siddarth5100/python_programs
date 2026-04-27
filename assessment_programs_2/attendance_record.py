# ----------------------------------------que 1
'''
Given a list of employee attendance records, 
write a program to find employees who were absent more than 2 days.
'''

attendance = [
    {"emp": "Ravi", "status": "Present"},
    {"emp": "Priya", "status": "Absent"},
    {"emp": "Ravi", "status": "Absent"},
    {"emp": "Priya", "status": "Absent"},
    {"emp": "Kumar", "status": "Absent"},
    {"emp": "Ravi", "status": "Absent"},
    {"emp": "Priya", "status": "Absent"},
    {"emp": "Ravi", "status": "Absent"},
]

# Expected output: ['Ravi', 'Priya']

attendance_count = {}
absent_employee = []

for employee in attendance:
    if employee["status"] == "Absent":
        if employee["emp"] not in attendance_count:
            attendance_count[employee["emp"]] = 1
        else:
            attendance_count[employee["emp"]] += 1

for emp, count in attendance_count.items():
    # print(emp, count)
    if count > 2:
        absent_employee.append(emp)

print(attendance_count)
absent_employee.sort(reverse=True)

print(absent_employee)
