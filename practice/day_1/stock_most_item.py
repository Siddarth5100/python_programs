stock = ["Mouse", "Keyboard", "Mouse", "Monitor", "Mouse", "Keyboard"]

stock_1 = {}
highest_count_item = ""

count = 0
for item in stock:
    if item not in stock_1:
        stock_1[item] = 0
    stock_1[item] += 1

for key, value in stock_1.items():
    if value > count:
        count = value
        highest_count_item = key

print(highest_count_item)