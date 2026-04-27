words = ["apple", "banana", "muskmelon", "grapes", "grapes", "orange", "mango", "apple", "orange", "banana", "apple", "mango"]

item_count = {}

for item in words:
    # print(item)
    if item not in item_count:
        item_count[item] = 0
    item_count[item] += 1
        
count = 0
item_name = ""

for key, val in item_count.items():
    # print(key, val)
    if val > count:
        count = val
        item_name = key

print(item_name, count)