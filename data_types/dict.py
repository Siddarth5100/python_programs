
# ----------------------------------------------------------- Que 1
# student = {}
# print(student, type(student))

# student["name"] = "Arun"
# print(student, type(student))

# student["age"] = 21
# print(student, type(student))

# student["grade"] = "A"
# print(student, type(student))

# # this is single data, how to add another data in another dict
# # eg: {'name': 'Arun', 'age': 22, 'grade': 'A', 'city': 'chennai', {}} how to add this empty one

# student["age"]= 22
# print(student)

# student["city"] = "Chennai"
# print(student)

# student.pop("grade")
# print(student)

# print(student["name"])
# print(student.keys())
# print(student.values())

# count = 0
# for stu in student.items():
#     print(student)
#     count += 1

# print(count)

# print(len(student))

# student["key"]= []
# print(student)

# ----------------------------------------------------------- Que 2

# marks = {
#     "Arun": 85,
#     "Bala": 90,
#     "Charu": 85,
#     "Divya": 95,
#     "Eshan": 90
# }

# print(marks)

# count= 0
# print("---------------",type(marks.items()))
# print("---------------",dir(marks.items()))

# for name in list(marks.items()):
#     print(type(name))
#     if name[1] == 85:
#         count += 1
# print(count)

# name = ""
# for student, mark in marks.items():
#     print(mark)
#     if mark == 90:
#         print(mark[0])
#         name = student
#         break

# print(name)

# marks["Farhan"]= 80
# print(marks)

# marks["A"]= []
# print(marks)

# marks.pop("Charu")
# print(marks)

# # how to sort?

# print(marks.items(), type(marks.items()), dir(marks.items()))

# # ----------------------------------------------------------- Que 3

# students = {
#     "S1": {"name": "Arun", "marks": 85},
#     "S2": {"name": "Bala", "marks": 90},
#     "S3": {"name": "Charu", "marks": 88}
# }

# print(students, type(students))

# # print(students["S2"]["marks"])
# students["S3"]["marks"] = 92
# # print(students["S3"]["marks"])
# students["S4"]= {"name": "Divya", "marks":95}
# # print(students)
# students.pop("S1")
# print(students)

# print(students["S3"])

# print(students["S4"]["name"])

# --------------------------------------------------


thisdict = {}

# print(thisdict, type(thisdict))
thisdict["brand"] = "Ford"

# print(thisdict)

thisdict["model"] = "Mustang"
# print(thisdict)

thisdict["year"] = 1964
# print(thisdict)

thisdict["new"] = {}
# print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'new': {}}

# print(thisdict["new"])

# --------------------------------------------------

myfamily= {}
# print(myfamily, type(myfamily))

child = ["child1", "child2", "child3"]

# myfamily["child1"] = {}
# # print(myfamily, type(myfamily))

# myfamily["child2"] = {}
# # print(myfamily, type(myfamily))

# myfamily["child3"] = {}
# print(myfamily, type(myfamily))

# for c in child:
#     print(c, type(c))
#     if not c in myfamily:
#         myfamily[c] = {}
#         print(myfamily, type(myfamily))

# --------------------------Apr 11----------------------------

# details = []
# # print(details, type(details))

# details.append({"name": "Sid"})
# # print(details, type(details))

# # print(details[0], type(details[0]))
# details.append({"marks": [80, 90]})
# # print(details)
# details.append({})
# # print(details)
# details.append([])

# # for detail in details:
# #     print(detail, type(detail))
# #     detail["name"] = "siddhu"
# #     break

# # print(details)

# # print(details[0], type(details[0]))
# details[0]["name"] = "siddhu"
# # print(details)

# # print(details[1]["marks"][0], type(details[1]["marks"]))
# details[1]["marks"].append(95)
# # print(details)

# # print(details[2], type(details[2]))
# details[2]["city"] = "CBE"
# # print(details, type(details))

# details[3].append("python")
# # print(details)

# # print(details[2], type(details[2]))
# details[2].pop("city")

# print(details)

# del details[3][0]
# print(details)
# del details[2]
# print(details)

# -----------------------------------------------------

# que 1
# a = [1,2,3]
# b = a
# b[0] = 100

# print(a)

# que 2
# a = [1, 2, 3]
# b = a.copy()
# print(b)
# b[0] = 100

# print(a)
# print(b) # do this once you unnderstand above print(a)

data = []
# print(data, type(data))

data.append({})
# print(type(data[0]))

data[0]["id"] = 1
# print(data[0]["id"])

data[0]["skills"]= []
# print(data[0]["skills"])

# print(data[0]["skills"], type(data[0]["skills"]))

data[0]["skills"].append("python")
data[0]["skills"].append("sql")
# print(data)

data.append({})
# print(type(data[1]))

data[1]["id"] = "2"
# print(data)

# print(data[1], type(data[1]))
data[1]["skills"]=[]
# print(data)

# c = {"skills": []}
# print(c, type(c))
# c["skills"].append("python")
# print(c)

# c = [{"skills": []}]

# print(c, type(c))
# print(c[0], type(c[0]))
# print(c[0]["skills"], type(c[0]["skills"]))

# c[0]["skills"].append("python")
# print(c)

data[1]["skills"].append("html")
# print(data[1]["skills"])
# print(data)

data[0]["skills"][1]= "mysql"
# print(data)

data[0]["skills"].pop(0)
# print(data)

data[1]["skills"].pop(0)
# print(data)

data[1]["skills"]

# print(data)

# for d in data:
#     print(d)
#     if d["skills"] == []:
#         del d["skills"]

# print(d)

if data[1]["skills"] == []:
    del data[1]

# print(data)


record = {"name": "sid", "scores": [10, 20]}
new = record

# print(record)
# print(new)
# print()

new["name"] = "ram"

# print(record)
# print(new)

# -----------------------------------------------------

transactions = [
    {"user": "sid", "amount": 100},
    {"user": "ram", "amount": 200},
    {"user": "sid", "amount": 50},
    {"user": "raj", "amount": 300},
    {"user": "ram", "amount": 100}
]

#  expected output

{
    "sid": 150,
    "ram": 300,
    "raj": 300
}

# print(transactions, type(transactions))           # list
# print(transactions[0], type(transactions[0]))     # dict

each_user_spent = {}

# print(each_user_spent, type(each_user_spent))     # dict

for trans in transactions:
    # print(trans["user"])
    if not trans["user"] in each_user_spent:
        # print(trans["user"])
        each_user_spent[trans["user"]] = trans["amount"]
        # print(trans["amount"])
# print(each_user_spent)


totals = {}
# print(totals, type(totals))       # dict
name = "sid"
# print(name, type(name))           # str
amount = 100
# print(amount, type(amount))       # int

# print(totals, type(totals))
totals[name] = amount
# print(totals, type(totals), totals["sid"])

amt = 50

totals["sid"] = totals["sid"] + amt

# print(totals)

# ----------------------------------------------------------------

data = {"a": 10, "b": 20}

# print(data, type(data))               # dict  {'a': 10, 'b': 20} <class 'dict'>

scores = [85, 92, 78]
total_marks = 0



# print(total_marks)
# print(avg)

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

grade_wise = {}

for student in students:
    if student["grade"] not in grade_wise:
        grade_wise[student["grade"]] = []    
    
    grade_wise[student["grade"]].append(student["name"])

# print(grade_wise) 

    


list_1 = [10, 23, 34, 45, 56, 60]

mylist = []

# print(mylist)
mylist.append("apple")
mylist.append("banana")
mylist.append("cherry")
mylist.append("apple")

# print(mylist)

# for idx, item in enumerate(mylist):
#     print(idx, item)
#     pass

# for item in range(len(mylist)):
#     print(item, mylist[item])

x = mylist.count("apple")
# print(x)


list_1 = [2, 3, 5, 6, 8, 11, 13]
# idx  =  0  1  2  3  4  5  6
# left right

