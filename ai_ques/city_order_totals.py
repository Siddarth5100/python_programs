orders = [
    {"city": "Chennai", "customer": "Arun", "amount": 250},
    {"city": "Mumbai", "customer": "Bala", "amount": 400},
    {"city": "Chennai", "customer": "Charu", "amount": 300},
    {"city": "Delhi", "customer": "Divya", "amount": 200},
    {"city": "Mumbai", "customer": "Eshan", "amount": 150},
    {"city": "Chennai", "customer": "Farhan", "amount": 100}
]

city = ""
total_amount = 0
final_order = {}

# not efficient extra for loops, for city in final_order:
for order in orders:
    if order["city"] not in final_order:
        final_order[order["city"]] = 0
    
    for city in final_order:
        if order["city"] == city:
            final_order[city] += order["amount"]

for key, val in final_order.items():
    if val > total_amount:
        total_amount = val
        city = key

print(f"City: {city}, has the highest order value: {total_amount}")

