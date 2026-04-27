employees = [
    {"name": "Ravi", "salary": 25000},
    {"name": "Meena", "salary": 30000},
    {"name": "Karthik", "salary": 28000}
]

highest_sal = 0
emp_name = ""

for employee in employees:
    if employee["salary"] > highest_sal:
        highest_sal = employee["salary"]
        emp_name = employee["name"]

print(highest_sal, emp_name)