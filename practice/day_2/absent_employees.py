'''
Find employees absent more than 2 times.
'''

attendance = [
    {"emp": "Ravi", "status": "Present"},
    {"emp": "Priya", "status": "Absent"},
    {"emp": "Ravi", "status": "Absent"},
    {"emp": "Priya", "status": "Absent"},
    {"emp": "Kumar", "status": "Absent"},
    {"emp": "Ravi", "status": "Absent"},
    {"emp": "Priya", "status": "Absent"},
]

employee = {}
emp_name = []

for emp in attendance:
    if emp["emp"] not in employee:
        employee[emp["emp"]] = 0
    
    if emp["status"] == "Absent":
        employee[emp["emp"]] += 1

for key, val in employee.items():
    if val >= 2:
        emp_name.append(key)
    
print(employee)
print(emp_name)