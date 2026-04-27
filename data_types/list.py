
# ------------------------------- Que 1
# numbers = []
# print(numbers, type(numbers))

# numbers.append(1)
# print(numbers, type(numbers))

# numbers.append(2)
# print(numbers, type(numbers))

# numbers.append(3)
# print(numbers, type(numbers))

# numbers.append(4)
# print(numbers, type(numbers))

# numbers.append(5)
# print(numbers, type(numbers))

# numbers.insert(0, 10)
# print(numbers)

# numbers[4] = 0
# print(numbers)

# print(numbers[0])
# print(numbers[-1])
# print(len(numbers))

# ------------------------------- Que 2

# fruits = []
# print(fruits)
# fruits.append("apple")
# print(fruits)
# fruits.append("banana")
# print(fruits)
# fruits.insert(2, "mango")
# print(fruits)
# fruits.append("orange")
# print(fruits)
# fruits.insert(2, "grapes")
# print(fruits)
# fruits[1]= "kiwi"
# print(fruits)

# print("fruits: ", fruits)
# print(fruits[0])
# print(fruits[-1])
# print(len(fruits))

# marks = [45, 67, 82, 67, 90, 45, 100]
# print("marks:", marks, type(marks))

# count = 0
# print("starting count:", count)
# for mark in marks:
#     print(mark)
#     if mark == 45:
#         count += 1
# print("final count: ", count)

# # how to find the index? 
# print("index", marks.index(67))
# marks.pop(0)

# marks.append(75)
# print(marks)

# # sort?
# marks.sort()
# print(marks)

# # reverse?
# marks.sort(reverse=True)
# print(marks)

# ------------------------------- Que 3

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[1][1])

# matrix[2][2]=10
# print(matrix)

# matrix[2].append(11)
# print(matrix)

# matrix[0].pop(1)
# print(matrix)

# print(matrix[1])
# print(matrix[2][3])

# ------------------------------- Que 4

# items = [10, 20, [30, 40, [50, 60]], 70]

# print(items)
# print(items[2])
# print(items[2][2])
# print(items[2][2][1])

# items[2][1]=400
# print(items)

# items.append(80)
# print(items)

# items[2][2].insert(1,55)
# print(items)

# items.pop(1)
# print(items)

# ------------------------------- Que 5

# employees = [
#     ["Arun", 25],
#     ["Bala", 30],
#     ["Charu", 28]
# ]

# print(employees)

# employees.append(["Divya", 26])
# print(employees)

# employees[1][1] = 31
# print(employees)

# del employees[2]
# print(employees)

# employees.insert(1, ["Eshan", 29])
# print(employees)

# print(employees[3][1])

# print(employees[1][0])