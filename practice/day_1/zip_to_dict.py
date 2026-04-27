items = ["Pen", "Book", "Bag"]
qty = [10, 5, 2]

item_details = {}

for item in range(len(items)):
    item_details[items[item]] = qty[item]

print(item_details)