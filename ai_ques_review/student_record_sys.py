'''
1. CREATE

Add a new student:

Name: "Deepa"
Age: 20
Marks: 85


'''

students = {
    "Arun": {"age": 20, "marks": 78},
    "Bala": {"age": 21, "marks": 88},
    "Charu": {"age": 22, "marks": 91}
}

students["Deepa"] = {"age": 20, "marks": 85}
# print(students)

# students["Deepa"] = {"age": 20, "marks": 85} if i want to overwrite and i want only this?
''' # this works right?
students = {"Deepa": {"age": 20, "marks": 85}}
print(students)
'''

'''
2. READ

Print all students in this format:

Name: Arun, Age: 20, Marks: 78
'''

for student in students:
    # print(f"Name: {student}, Age: {students[student]["age"]}, Marks: {students[student]["marks"]}")
    pass

'''
3. UPDATE
Increase Bala's marks by +5
Update Charu's age to 23
'''

for student in students:
    if student == "Bala":
        students[student]["marks"] = students[student]["marks"] + 5
    
    if student == "Charu":
        students[student]["age"] = 23

# print(students)

'''
4. DELETE

Remove student:

"Arun"
'''

students.pop("Arun")
print(students)

for student in students:
    if student == "Arun":
        # students.pop(student) how to remove im getting error
        '''
        RuntimeError: dictionary changed size during iteration => pop
        RuntimeError: dictionary changed size during iteration => del
        '''
        pass 

# print(students)

highest = 0
name = ""
for student in students:
    if students[student]["marks"] > highest:
        highest = students[student]["marks"]
        name = student

# print(f"Topper: {name}, Marks: {highest}")
