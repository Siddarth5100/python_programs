
attendance = {
    "Arun": ["P", "P", "A", "P", "P"],
    "Bala": ["A", "A", "P", "P", "A"],
    "Charu": ["P", "P", "P", "P", "P"],
    "Deepa": ["A", "P", "A", "A", "P"]
}

'''
1. Find total PRESENT days for each employee
Arun: 4
'''

present_detail = {}

for emp in attendance:
    if emp not in present_detail:
        present_detail[emp] = 0
    
    count = 0
    for status in attendance[emp]:
        if status == "P":
            count += 1
    present_detail[emp] = count

for key, val in present_detail.items():
    # print(f"{key}: {val}")
    pass

'''
2. Find employee with HIGHEST attendance
Best Attendance: Charu - 5 days
'''

high_count = 0
emp_name = ""
for key, val in present_detail.items():
    if val > high_count:
        high_count = val
        emp_name = key

# print(f"Best Attendance: {emp_name} - {high_count} days")

'''
3. Print employees with attendance LESS THAN 3
Bala
Deepa
'''

for key, val in present_detail.items():
    # print(key, val)
    if val < 3:
        # print(key)
        pass

'''
4. Add BONUS Create a new dictionary:
Rules:

attendance >= 4 → bonus = 1000
attendance >= 3 → bonus = 500
else → 0
'''

new_dict = {}

for key, val in present_detail.items():
    # print(key, val)
    if val >= 4:
        new_dict[key] = 1000

    elif val >= 3:
        new_dict[key] = 500

    else:
        new_dict[key] = 0

print(new_dict)