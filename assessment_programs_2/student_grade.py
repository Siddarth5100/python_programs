'''
# que:

students = [
    {"name": "Akash", "grade": "A"},
    {"name": "Bala", "grade": "B"},
    {"name": "Chandru", "grade": "A"},
    {"name": "Divya", "grade": "B"},
    {"name": "Farhan", "grade": "C"}
]

# expected output:
{"A": ["Akash","Chandru"], "B": ["Bala", "Divya"], "C": ["Farhan"]}
'''

students = [
    {"name": "Akash", "grade": "A"},
    {"name": "Bala", "grade": "B"},
    {"name": "Chandru", "grade": "A"},
    {"name": "Divya", "grade": "B"},
    {"name": "Farhan", "grade": "C"}
]

# print(students, type(students))           list type
# print(students[0], type(students[0]))     dict type inside list

student_grade_wise = {}                     # dictionary
# print(student_grade_wise, type(student_grade_wise))   dict

# print(dir(dict))                          to check the attributes

for student in students:
                                                                    # print(student, type(student))         dict => {'name': 'Akash', 'grade': 'A'} <class 'dict'>
                                                                    # print(student["grade"])
    if not student["grade"] in student_grade_wise:
                                                                    # print(student["grade"])           A
        student_grade_wise[student["grade"]] = []
                                                                    # print(student_grade_wise)         # {'A': [], 'B': [], 'C': []}

    # if student["grade"] in student_grade_wise:
    student_grade_wise[student["grade"]].append(student["name"])

print(student_grade_wise)