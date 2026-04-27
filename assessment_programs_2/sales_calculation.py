# ----------------------------------------que 2
'''
Given a list of sales, write a program that groups items by category 
and finds the category with the highest total sales value.
'''

sales = [
    {"item": "Pen", "category": "Stationery", "amount": 200},
    {"item": "Chair", "category": "Furniture", "amount": 5000},
    {"item": "Notebook", "category": "Stationery", "amount": 150},
    {"item": "Desk", "category": "Furniture", "amount": 8000},
    {"item": "Marker", "category": "Stationery", "amount": 300},
    {"item": "Monitor", "category": "Electronics", "amount": 12000},
]

# Expected output: Electronics - 12000

category = {}
total_sales_value = 0
category_name = ""

for sale in sales:
    if sale["category"] not in category:
        category[sale["category"]] = {}

    # print(sale["category"], sale["item"], sale["amount"])     Stationery Pen 200
    category[sale["category"]][sale["item"]] = sale["amount"]    
    # category = {'Stationery': {'Pen': 200, 'Notebook': 150, 'Marker': 300}, 'Furniture': {'Chair': 5000, 'Desk': 8000}, 'Electronics': {'Monitor': 12000}}
    
# print(category, type(category))
for key, value in category.items():
    total = 0
    # print(value, type(value))
    for amount in value.values():
        # print(amount)
        total += amount
        # print(total)
    
    if total > total_sales_value:
        total_sales_value = total
        category_name = key
    
print(f"Category : {category_name}, Total sales value : {total_sales_value}")
# print(category)