orders = [
    {"item": "Pen", "qty": 10, "price": 5},
    {"item": "Book", "qty": 3, "price": 40},
    {"item": "Bag", "qty": 1, "price": 500}
]

total_bill = 0

for order in orders:
    cal_price = order["qty"] * order["price"]
    total_bill += cal_price

print(total_bill)