import copy
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = []

# c.append(a)
# c.append(b)

# d = copy.deepcopy(c)
# print(d)

# a.append(4)
# print(c, d)

a = [1, 2, 3]
# print(a, id(a))

b = a
# print(b, id(b))

c = a.copy()
# print(c, id(c))

a.append(4)
# print(a, id(a))
# print(b, id(b))
# print(c, id(c))

d = []
d.append(a)
d.append(b)
print(d)

a.append(4)
print(d)