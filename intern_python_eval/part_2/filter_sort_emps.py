'''
Q7. Filter & Sort Employees
Covers: List of Dicts

Scenario: From the employee list, return Engineering employees earning more than Rs. 50,000, sorted
by salary (highest first).

employees = [
{'name': 'Arjun', 'dept': 'Engineering', 'salary': 65000},
{'name': 'Bala', 'dept': 'Sales', 'salary': 45000},
{'name': 'Chitra', 'dept': 'Engineering', 'salary': 48000},
{'name': 'Divya', 'dept': 'Engineering', 'salary': 72000},
{'name': 'Ezhil', 'dept': 'Engineering', 'salary': 55000}
]

Expected Output:
[
{'name': 'Divya', 'dept': 'Engineering', 'salary': 72000},
{'name': 'Arjun', 'dept': 'Engineering', 'salary': 65000},
{'name': 'Ezhil', 'dept': 'Engineering', 'salary': 55000}
]
'''

employees = [
{'name': 'Arjun', 'dept': 'Engineering', 'salary': 65000},
{'name': 'Bala', 'dept': 'Sales', 'salary': 45000},
{'name': 'Chitra', 'dept': 'Engineering', 'salary': 48000},
{'name': 'Divya', 'dept': 'Engineering', 'salary': 72000},
{'name': 'Ezhil', 'dept': 'Engineering', 'salary': 55000}
]


emp_sort = []

for employee in employees:
    if employee["dept"] == "Engineering" and employee["salary"] > 50000:
        emp_sort.append(employee)

print(emp_sort)

#  16:32
# how to sort?
# 16:40