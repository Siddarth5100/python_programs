sales = [
    {"item": "Pen", "category": "Stationery", "amount": 200},
    {"item": "Chair", "category": "Furniture", "amount": 5000},
    {"item": "Notebook", "category": "Stationery", "amount": 150},
    {"item": "Desk", "category": "Furniture", "amount": 8000},
    {"item": "Monitor", "category": "Electronics", "amount": 12000}
]

sales_res = {}

for sale in sales:
    if sale["category"] not in sales_res:
        sales_res[sale["category"]] = 0

    sales_res[sale["category"]] += sale["amount"]

print(sales_res)