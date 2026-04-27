name = "siddarth"
res = {}

for char in name:
    if char in res:
        res[char] += 1
    else:
        res[char] = 1

print(res)

names = "john DOE, JANE smith, Bob JOHNSON, alice WILLIAMS"

name = names.title()
# print(name)
name_title = name.split(",")
print(name_title)

