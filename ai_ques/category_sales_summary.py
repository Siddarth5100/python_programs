sales = [
    {"item": "Pen", "category": "Stationery", "amount": 50},
    {"item": "Notebook", "category": "Stationery", "amount": 100},
    {"item": "Chair", "category": "Furniture", "amount": 500},
    {"item": "Pencil", "category": "Stationery", "amount": 20},
    {"item": "Table", "category": "Furniture", "amount": 700},
    {"item": "Eraser", "category": "Stationery", "amount": 10}
]

'''
expected output

{
    "Stationery": 180,
    "Furniture": 1200
}
'''

total_sales_amount = {}
category_name = ""
max_amount = 0

for sale in sales:
    if sale["category"] not in total_sales_amount:
        total_sales_amount[sale["category"]] = 0

    total_sales_amount[sale["category"]] += sale["amount"]

for key, val in total_sales_amount.items():
    if val > max_amount:
        max_amount = val
        category_name = key

'''
# 1st way of solution
but not efficient, too many loops, nested loops
'''

# for sale in sales:
#     if sale["category"] not in total_sales_amount:
#         total_sales_amount[sale["category"]] = 0

# for category in total_sales_amount:
#     total_amount = 0

#     for sale in sales:
#         if category == sale["category"]:
#             total_amount += sale["amount"]
#             total_sales_amount[sale["category"]] = total_amount

# print(f"Category Name: {category_name}, Maximum amount: {max_amount}")