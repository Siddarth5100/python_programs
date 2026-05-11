'''
2.Given a list of sales, 
write a program that groups items by category and 
finds the category with the highest total sales value.
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

sales_category = {}

for sale in sales:
    if not sale["category"] in sales_category:
        sales_category[sale["category"]] = 0

    total = 0
    for category in sales_category:
        if category == sale["category"]:
            sales_category[category] += sale["amount"]

print(sales_category)

catego = ""
high_val = 0

for key, val in sales_category.items():
    if val > high_val:
        high_val = val
        catego = key

print(f"{catego}, {high_val}")