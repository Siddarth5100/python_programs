# to check memory address of a varible
'''
x = 42
print(id(x))

a = [1,2,3]
b = a
print("a:", a, id(a))
print("b:", b, id(b))
'''

# pyhton complier, how it works
'''
x = 10
print(x)
print('a')

def test():
    i = 20
    x = 20
    print(x)
    def test1():
        print(i)

    test1()

print('a')
print('x',x)
test()
'''

# string
'''
a = "Siddarth"
print(a)
print(a[0])
print(a[3])
# a[3] = "b"
print(a)
a.replace("d", "b")

print(a)
'''

# to understand the difference between is & ==
'''
a = [1,2,3]
b = a

print("a:", a, id(a))
print("b:", b, id(b))

print(a is b)
print(a == b)

x = [1,2]
y = [1,2]

print(x is y)
print(x == y)
'''

# ----------------------------------------------------
def add_num(a, b):
    c = a + b
    return c

def get_arithmetic():
    return add_num(2, 3)


# print(get_arithmetic())

scores = [40, 3, 28]

# for score in scores:
#     if not isinstance(score, int):
#         print("error")
#     else:
#         print(score)

a = 10 and 5
# print(a)

a = 0 and 5
# print(a)

# print(0 and 10)

# --------------------------------------------------------------------

# names = []
# students = {}

# print(names, type(names))
# print(students, type(students))

# students["name"] = "JC"
# test = {"name": "test"}

# print(students, type(students))
# print(test, type(test))

# students["age"] = 0
# print(students)
# students["new_dict"] = {}
# print(students["new_dict"], type(students["new_dict"]))

# students["new_dict"]["hobby"] = []
# print(students)

# details = {
#     "name": "sid",
#     "age": 30
# }

# print(details, type(details))

# details["education"] = {
#     "10th": "Perks",
#     "12th": "Kennedy",
#     "ug": "SNR",
#     "pg": "Sri Ramakrishna"
# }

# print(details, type(details))
students = []

# add_name = students["name"] = "Sidd"

# students.append(add_name)

stu = {"name": "siddarth"}

s = {}

s["name"] = "jc"

# print(students, type(students))
# print(stu, type(stu))
# print(s, type(s))

s_tu = {}

s_tu["name"] = "sid"

# print(s_tu)



students = []

student = {}

student["name"] = "siddarth"

students.append(student)

# print(students)

#---------------------------------------------------------------------

names = []

names.append("Siddarth")
names.append("Akash")
names.append("Bala")


details = {}

details["name"] = "Chandru"
details["age"] = 30


nums = [10, 20, 30, 40]

count_num = 0
for num in nums:
    # print(num)
    count_num += num


data = ["a", "b", "a", "c", "a"]

count_a = 0

for a in data:
    # print(a)

    if a == "a":
        count_a += 1


student = {"name": "sidd"}

student["city"] = "Chennai"

students = ["Sidd", "Ram", "Sidd", "Abi"]

stu = []

for name in students:
    # print(name)
    if not name in stu:
        stu.append(name)


marks = {"math": 80, "eng": 90, "sci": 70}

higest_mark = 0

for mark in marks.values():
    # print(mark, type(mark))
    if higest_mark <= mark: # how to check what it returns?
        higest_mark = mark


list_of_dict = []

details = {"name": "JC"}

list_of_dict.append(details)

details["age"] = 30
details["education"] = "Msc" 
# here i dint access list right? how it is getting appended  


students = [
    {"name": "Sidd", "marks": 80},
    {"name": "Ram", "marks": 90}
]

# print(students[1]["name"])


data = [1, 2, 3, 4, 5]

even_data = []

for num in data:
    if num % 2 == 0:
        even_data.append(num)


data = [[1, 2], [3, 4], [5, 6]]
final_data = []

for no in data:
    for num in no:
        final_data.append(num)
    

students = {
    "s1": {"name": "Sidd", "marks": 80},
    "s2": {"name": "Ram", "marks": 90}
}

# print(students["s2"]["name"])


# ques = 13 total marks? i want to count 80 + 90?

data = {"a": 10, "b": 20}

swap_data = {}
# print(data)

for key, value in data.items():
    # print(key)
    swap_data[value] = key


students = [
    {"name": "Sidd", "marks": [80, 90]},
    {"name": "Ram", "marks": [70, 60]}
]

# final_list = []

# for student in students:
#     print(student, type(student), "------------")
#     print(student["marks"], type(student["marks"]))
#     total_mark = 0
#     for marks in student["marks"]:
#         print(marks)
#         total_mark += marks

#     print(total_mark)

# last que
'''
we want to calculate the marks 1st
once done we want to compare the total marks
'''

# print(students, type(students))

details = []


employees = [
    {"name": "A", "salary": 1000},
    {"name": "B", "salary": 2000},
    {"name": "C", "salary": 1500}
]

total_salary = 0

for employee in employees:
    total_salary += employee["salary"]

# print(total_salary)


employees = [
    {"name": "A", "salary": 1000},
    {"name": "B", "salary": 2000},
    {"name": "C", "salary": 1500},
    {"name": "C", "salary": 3500}
]

high_salary = 0

for employee in employees:
    if employee["salary"] >= high_salary:
        high_salary = employee["salary"]

# print(high_salary)

students = [
    {"name": "A", "marks": [10, 20]},
    {"name": "B", "marks": [30, 5]},
    {"name": "C", "marks": [15, 15]},
    {"name": "D", "marks": [15, 45]}
]

highest_total = 0
name = ""

for student in students:
    total_marks = 0
    for marks in student["marks"]:
        total_marks += marks
    
    if total_marks >= highest_total:
        highest_total = total_marks
        name = student["name"]

# print(name)

[{"name": "Sidd", "age": 20}]


# my_info = []
# print(id(my_info))

# details = {}
# print(my_info)
# print(id(details))

# my_info.append(details)

# print(my_info, type(my_info))
# print(my_info[0], type(my_info[0]))

# details["name"] = "Siddarth"
# print(id(details))
# print(my_info)
# details["age"] = 20
# print(my_info)

# ----------------------------------------------------------

products = [
    {"name": "Pen", "price": 10},
    {"name": "Book", "price": 50},
    {"name": "Bag", "price": 40}
]

product_name = ""
highest_price = 0

for product in products:
    if product["price"] >= highest_price:
        highest_price = product["price"]
        product_name = product["name"]

# print(f"This product {product_name}, has the highest price {highest_price}")


items = [
    {"name": "A", "qty": 2},
    {"name": "B", "qty": 5},
    {"name": "C", "qty": 3}
]

quantities = 0

for item in items:
    # print(item["qty"])
    quantities += item["qty"]

# print(f"Total quantities = {quantities}")

a = {"x": 10}
b = a
b["y"] = 20
# print(a)
# print(b)

{"x": 10, "y": 20}

'''
a has a value
b has the same memory value
if anything gets changed
both will change
'''

# --------------------------------------------------------------

data = [[10, 20], [30, 40], [50]]

total_of_all_nums = 0

for number in data:
    for num in number:
        total_of_all_nums += num

# print(f"Total of all nums: {total_of_all_nums}")


students = {
    "s1": {"name": "Sidd", "mark": 85},
    "s2": {"name": "Ram", "mark": 92},
    "s3": {"name": "Abi", "mark": 88}
}

student_name = ""
highest_mark = 0


for key, value in students.items():
    if value["mark"] > highest_mark:
        highest_mark = value["mark"]
        student_name = value["name"]

# print(student_name, highest_mark)


'''
[
    {"name": "A", "score": 10},
    {"name": "B", "score": 20},
    {"name": "C", "score": 30}
]
'''

names = ["A", "B", "c"]
scores = [10, 20, 30]

expec_list = []

for name in names:
    n = {"name": name}
    expec_list.append(n)
    
# print(expec_list)


teams = [
    {"team": "Red", "scores": [10, 20, 30]},
    {"team": "Blue", "scores": [25, 25, 20]},
    {"team": "Green", "scores": [15, 15, 15]}
]

highest_total_score = 0
team_name = ""

for team in teams:

    total_score = 0
    for score in team["scores"]:
        total_score += score
    
    if total_score > highest_total_score:
        highest_total_score = total_score
        team_name = team["team"]

# print(highest_total_score, team_name)


records = []
student = {"name": "Sidd"}

records.append(student)     # here memory val gets equal right
student = {"name": "Ram"}

# print(records)

[{"name": "sidd", "name": "Ram"}]
'''
due to memory gets shared,
if anything gets changed,
gets reflected in both
'''



employees = {"emp": "Ravi", "status": "Present"}

count = 0 
if employees["status"] == "Present":
    count += 1

# print(count)

''' 

nums = [4, 0, 7, 0]

print(nums)
for num in nums:
    print(num)

for num in enumerate(nums):     # other than enumerate any other option is there? to get index + value
    print(num)

for idx, val in enumerate(nums):
    print(idx, val)

nums = [0, 3, 0, 5, 8, 0, 2]

count = 0
for num in nums:
    print(num)
    if num == 0:
        count += 1
print(count)

nums = [0, 3, 0, 5]

for idx, val in enumerate(nums):
    print(idx, val)
    if nums[idx] == 0:
        nums[idx] = -1
print(nums)

nums = [0, 3, 0, 5]

for idx, val in enumerate(nums): 
    # print(idx, val)
    if nums[idx] != 0:
        print(nums[idx])


print(len(nums))
'''

nums = [1, 2, 3, 4]

for x in nums:
    # print(x)
    if x == 2:
        nums.remove(2)
# print(nums)


my_dict = {"state": "tamilnadu", "city": "cbe"}
city = my_dict.get("city", "testing") 

# print(city)

def large_num(nums_list):
    highest_num = 0
    sec_high = 0

    for num in nums_list:
        # print(num)
        pass


large_num([4, 7, 2, 7, 9, 5, 9])


nums = [3, 5 , 0, 1, 0, 0, 2]

# type 1(praveen)
in_pos = 0

for num in nums:
    # print(num, type(num))

    if num != 0:
        nums[in_pos] = num
        in_pos += 1

for i in range(in_pos,len(nums)):
    nums[i] = 0

# print(nums)

def prime_factors():
    number = int(input("Enter the number: "))
    prime_factor = []

    while number % 2 == 0:
        prime_factor.append(2)
        number = number // 2

    divisor = 3

    while divisor * divisor <= number:
        if number % divisor == 0:
            prime_factor.append(divisor)
            number = number / divisor

        else:
            divisor += 1

    return prime_factor
    

# print(prime_factors())

# --------------------------
c = 20


a = 10 + c
b = a

# print(a, type(a), id(a))
# print(b, type(b), id(b))


# print(a, id(a))
# print(b, id(b))

a = [1, 2]
b = a
c = b

a.append(3)
# print(c)    # [1, 2, 3]

# print(a, type(a), id(a))
# print(b, type(b), id(b))
# print(c, type(c), id(c))


a = [1, 2]
b = a

a = a + [3]

# print(b)    # [1, 2]

a = [1, 2]
b = a

b += [3]

# print(a)    # [1, 2]

# b = b + [3]
# b = [1, 2] + [3]

# print(a, id(a))
# print(b, id(b))


a = [1, 2]
b = [1, 2]

# print(a is b)   # False
# print(a == b)   # True

def update(x):  # x = [1, 2]
    x += [10]   # x = x + [10] => if add happens will this be the output [1, 2, 10]?
                

a = [1, 2]
update(a)

# print(a)    # [1, 2, 10]

def update(x):
    x = x + [10]

a = [1, 2]
update(a)

# print(a)    # [1, 2, 10]

a = [[1, 2], [3, 4]]
b = a.copy()

a[0].append(99)

# print(b)    # [[1, 2], [3, 4]]

# print(a, id(a))
# print(b, id(b))


a = [1, 2, 3]
b = a

a.pop()
b.append(10)

# print(a)    # [1, 2, 10]

a.append(5)
a = a + [5]
a.copy()
a.sort()


a = [1, 2, 3]
b = a.copy()

a.append(4)
b.append(5)

# print(a, b)     # [1, 2, 3, 4] [1, 2, 3, 4, 5]

a = [1, 2, 3]
b = [1, 2]
# print(a+b)
c = a.append(4)

a = [1]
b = a
a += [2]
# print(a)
# print(b)

a = [1]
b = a
a = a + [2]
# print(a)
# print(b)

a = 1
b = a
a += 2
# print(a)
# print(b)

a = 1
b = a
a = a + 2
# print(a)
# print(b)

#-----------------------------------------------------
a = [1]
b = a       # [1]
a += [a]    # a = a + 1 a = [1] + [1]    [1, 1]

# print(a, id(a))
# print(b, id(b))    # [1, 1]

a = [1]
b = a
a = a + [2]        # [1]

# print(a, id(a))
# print(b, id(b))

a = [[1], [2]]
b = a.copy()

b[0].append(5)

# print(a, id(a))    # [[1, 5], [2]]
# print(b, id(b))

a = [1, 2]
b = a.copy()

b = [10, 20]

# print(a)


# a = "hello"
# print(a)

# a[0] = "H"
# print(a)

t = (1, 2, 3)
# t[0] = 10

# print(t)

s = {1, 2, 2, 3}
# print(s)

s = {"a": 1}
# s.get()

# for ch in "abc":
#     print(ch)

s = set([1,1,2,3, 3])
# print(type(s), len(s))

# for ch in "hi":
#     print(ch)

a = [1, 2, 3]
# print(a * 2)    # [2, 4, 6]

a = [[0]*3]*3   # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][0] = 1     # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

# print(a)    # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

# ans => [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

data = {"a": 1, "b": 2}
data["a"] = 100

# print(data)     # {"a": 100, "b": 2}

data = {1: "a", 1: "b", 1: "c"}
# print(data)     # key should be unique => {1: "c"}

data = {"a": 1, "b": 2}

# for x in data:
#     print(x)

a = "abc"
b = a

# print(a, id(a))
# print(b, id(b))

a = a + "d"

# print(a, id(a))
# print(b, id(b))


# print([1, 2] * 3)

# [1, 2], [1, 2], [1, 2]
# ans i got => [1, 2, 1, 2, 1, 2]
# so this will happen in same list

# a = 0

# if a:
#     print("Yes")
# else:
#     print("No")

# # No as value 0 denotes False

# a = 5

# if a > 2 and a < 10:
#     print("A")
# else:
#     print("B")

# # A Both coditions satisified (and => both should satisify)

# a = 5

# if a > 10 or a == 5:
#     print("A")
# else:
#     print("B")

# # A 2nd condotion satisified (or => either one)

# name = ""

# if name:
#     print("Filled")
# else:
#     print("Empty")

# # Empty "" empty string like 0 so false

# num = 7

# if num % 2 == 0:
#     print("Even")
# else:
#     print("False")

# # False 7 % 0 != 0

# # if num == 1 or 2 or 3:
# # 2 and 3 there is no comparison or num == 2 or num == 2
# # we want to return/print something that also we dint do

# # Q8 none of the above (i dint try the combinations like this)

# a = "Hello"

# if not a:
#     print("Empty")
# else:
#     print("Has Value")

# # Has Value string has value, so will get True

# age = 17

# def check_age(age):
#     if age < 18:
#         print("Age must be atleast 18, and ID req")
#     else:
#         print("Done")
    
# check_age(age)

# ---------------------------------------------------------------

for i in range(3):
    # print(i)
    pass

# 0, 1, 2 i takes nos from 0 till what we mentioned range syntax? 
# start, end if we mention 1,3 it will start from there 1 untill 3
# means 2 it will not go to the last val mentioned
# (start, stop, step) test sytax too

# 1, 2, 3, 4

# 1,3,5,7,9

# value 10, 20, 30

# len(nums) => 3
# nums[0] => 10 nums[1] => 20 num[2] => 30
# i index

# index, value
# 0 10, 1 20, 2 30

for i in range(5):
    if i == 3:
        break
    # print(i)
# 3 print we given after break right?

# 0, 1, 2, 3 

nums = [1, 2, 3]

for i in nums:
    i = i + 10

# print(nums)
# [1, 2, 3] because we dint update in main var, it is a loop with temp var

# when we want direct value will use for num in list
# when we want index val will use range(len(list))


for i in range(4):
    if i == 2:
        break
    # print(i)

# 0, 1

for i in range(4):
    if i == 2:
        continue
    # print(i)

# 0, 1, 3

# break will stop the loop
# continue will skip only the iteration

nums = [10, 20, 30]

for i, v in enumerate(nums):
    nums[i] = v + 5

# print(nums)

# 15, 25, 35

# -----------------------DSA------------------------------------

for i in range(2):
    for j in range(2):
        # print(i, j)
        pass

# 1st line 0, 1
# 2nd line 0, 1

# 0, 0  0, 1  1, 0  1, 1

for i in range(3):
    # print(i)
    # print()
    for j in range(i):
        # print(j)
        # print("*", end="")
        pass

# 0, 1, 2
# i cant structure it
#  0, 1
#  *

nums = [1, 2, 3]

for i in nums:
    for j in nums:
        if i != j:
            # print(i, j)
            pass

# 1 123, 2 123, 3 123
# 2, 3 1, 3 1, 2

for i in range(3):
    for j in range(3):
        if j == 1:
            break
        # print(i, j)

# 012
# 012
# 0 012 1 012 2 012

# 00

i = 0
while i < 3:
    # print(i)
    i += 1

# 0 1 2

nums = [1, 2, 3, 4]

for num in nums:
    if num % 2 == 0:
        # print(num)
        pass

# 2, 4

nums = [1, 2, 2, 3]

count = 0
for num in nums:
    if num == 2:
        count += 1

# print(count)

for i in range(2):
    # print(i)
    for j in range(3):
        # print(j)
        # print(i, j)
        pass

# 0, 1
# 0, 1, 2
# 6 times

'''
0 0
0 1
0 2
1 0
1 1
1 2
'''

for i in range(2):
    for j in range(3):
        # print("*")
        pass

# 0 1
# 0 1 2
'''
same above
'''
# *
# **
# 3 stars, gets printed

for i in range(3):
    # print(i)
    pass

# 0, 1, 2

nums = [1, 2, 3, 4]
for num in nums:
    if num > 2:
        # print(num)
        pass

# 3 4

for i in range(3):
    # print(i)
    pass

# count

nums = [1, 2, 3, 4]

for num in nums:
    if num % 2 == 0:
        # print(num)
        pass

# filter

nums = [1, 2, 3, 4]

count = 0
for num in nums:
    if num == 2:
        count += 1

# count
# print(count)

nums = [1, 2, 3]

for i in nums:
    for j in nums:
        # print(i, j)
        pass

# pairing

for i in range(2):
    for j in range(3):
        # print("*")
        pass

# 6

for i in range(3):
    for j in range(2):
        # print(i, j)
        pass

# 0, 1, 2
# 0, 1
'''
0 0
0 1
1 0
1 1
2 0
2 1
'''

# 6

for i in range(3):
    for j in range(2):
        if j == 1:
            break
        # print(i, j)

# i => 0, 1, 2
# j => 0, 1
'''
0 0
0 1
1 0
'''

# ----------------------string ques--------------------------------

word = "hello"

for char in word:
    # print(char)
    pass

word = "python"

for letter in range(len(word) + 1):
    # print(letter)
    # for char in (len(word) - 1):
        # print(char)
        pass
# how to do reverse string manually?

word = "banana"

count = 0
for char in word:
    # print(char)
    if char == "a":
        count += 1
# print(count)

word = "hello123"

for char in word:
    # print(char.isalpha())
    if char.isalpha():
        # print(char)
        pass
# any other way

word = "level"
'''
level
level reverse the string then compare both
'''

# reverse = ""
# for letter in range(len(word)):
#     # print(letter)
#     for char in range(len(word) - 1):
#         print(char)
# want to learn/practice reverse

word = "aabbc"

count_freq = {}

for char in word:
    # print(char)
    if not char in count_freq:
        count_freq[char] = 0
        # want to learn/practice more how to count it
    if char in count_freq:
        count_freq[char] += 1

# print(count_freq)

word = "programming"

word_1 = ""
'''
progamin
'''
for char in word:
    # print(char)
    for letter in word:
        # print(letter)
        if char == letter:
            word_1 = letter
        # want learning and practice

# print(word_1)


word = "python"
'''
p y t h o n
0 1 2 3 4 5

n o h t y p
5 4 3 2 1 0
'''

reversed_word = ""

for num in range(len(word)-1, -1, -1):
    # print(num)
    reversed_word += word[num]

# print(reversed_word)

word = "programming"
'''
expec => p r o g a m i n
'''
remove_word = ""

for char in range(len(word)):
    if not word[char] in remove_word:
        remove_word += word[char]

# print(remove_word)

# -------------------------------------------------

word = "banana"

for char in range(len(word) -1, -1, -1):
    # print(len(word) - 1)
    # print(word[char])
    pass

'''
i got the ans but
actually i dint understand this
how this works? range(len(word) -1, -1, -1)
where to print(to see the count reducing on each loop?)
range() syntax? params to pass
start stop increment that's it right?
if range(5)
=> auto start from 0 => 0, 1, 2, 3, 4
if range(10, 16)
=> 10, 11, 12, 13, 14, 15
if range(10, 16, -1)
=> 10, 12, 14, 15
'''

nums = [10, 20, 30, 40]

'''
manual step
take the nums list
[40, 30, 20, 10]
from reverse i added

psudeo code
take the list
# how to do in same list?
'''
nums_1 = []

for num in range(len(nums) -1, -1, -1):
    nums_1.append(nums[num])

# print(nums)
# print(nums_1)

word = "a1b2c3"
reverse_word = ""

# print("len:", len(word), "minus val:", (len(word) - 1))
for char in range(len(word)-1, -1, -1):
    # print(char)
    # print(word[char])
    reverse_word += word[char]

# print(word)
# print(reverse_word)

word = "madam"
reverse_word = ""

for char in range(len(word)-1, -1, -1):
    # print(word[char])
    reverse_word += word[char]
    
# if word == reverse_word:
#     print("It is palindrome")
# else:
#     print("It is not palindrome")

# print(word)
# print(reverse_word)

# as mentioned will do que 5

# for i in range(10, 14, -1):
#     print(i)

# for i in range(19, 14, -1):
#     print(i)

nums = [10, 20, 30, 40, 50]
# print(nums)

for num in nums:
    # print(num)
    pass

'''
same list reverse teach me then will do the practical one
simple, easy to understand
'''

word = "apple"

# for char in range(len(word) -1, -1, -1):
#     # print(char)
#     print(word[char], char)

nums = [10, 20, 30, 40, 50]

left = 0
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

# print(nums)

# --------------------------range practice-------------------------

for i in range(5):
    # print(i)
    pass

'''
expec_out => 0 1 2 3 4
start => default value 0
end => 5, so it stops before 5 => 4
it print from 0 to 4
'''

for i in range(2, 7):
    # print(i)
    pass

'''
expec_out => 2 3 4 5 6
start val => 2, it start from 2
end val => 7, so it print until 7 => 6
'''

for i in range(10, 4, -1):
    # print(i)
    pass

'''
expec_out => 10 9 8 7 6 5
as this is reverse one start val should be larger than stop
start val => 10 it starts from 10
stop val => 4 until 4 => 3
increment => -1 from back
'''

for i in range(0, 10, 2):
    # print(i)
    pass

'''
expec_out => 0 3 6 9
start => 0 starts from 0
end => 10 until 9
increment => 2 +2
''' 

for i in range(5, -1, -2):
    # print(i)
    pass

'''
expec_out => dont know
start => 5, as this is reverse start should be greater
end => -1
increment => -2
'''

for i in range(1, 5, -1):
    # print(i)
    pass

'''
nothing, if reverse starting num should be greater
'''
