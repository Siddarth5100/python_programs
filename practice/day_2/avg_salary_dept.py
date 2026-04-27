'''
Find average salary department-wise.
'''

employees = {
    "Ravi": {"dept": "HR", "salary": 25000},
    "Meena": {"dept": "IT", "salary": 40000},
    "Kumar": {"dept": "IT", "salary": 35000},
    "Anu": {"dept": "HR", "salary": 28000}
}

emp_detail = {}

for emp in employees:
    if employees[emp]["dept"] not in emp_detail:
        emp_detail[employees[emp]["dept"]] = {}
        emp_detail[employees[emp]["dept"]]["salary"] = 0
        emp_detail[employees[emp]["dept"]]["count"] = 0
    
    emp_detail[employees[emp]["dept"]]["salary"] += employees[emp]["salary"]
    emp_detail[employees[emp]["dept"]]["count"] += 1

# print(emp_detail)

avg = 0
for dept, val in emp_detail.items():
    avg = val["salary"] / val["count"]
    
    print(dept, avg)