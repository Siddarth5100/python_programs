'''
Merge repeated items and calculate final quantity per item.
'''

cart = [
    {"item": "Pen", "qty": 2, "price": 10},
    {"item": "Book", "qty": 1, "price": 50},
    {"item": "Pen", "qty": 3, "price": 10}
]

cart_res = {}

# how to create multiple dict, multiple key in for loop

'''
pen 10 2 + 3 

cart_res {"pen": 2, qty: 2} in next loop 5
now i want to add for book but qty key should not duplicate
i want to use a dict of dict or?
idea??
'''

for item in cart:
    if item["item"] not in cart_res:
        cart_res[item["item"]] = {}
        # how to count the current_qty?
        cart_res[item["item"]]["qty"] = 0
    
    cart_res[item["item"]]["qty"] += item["qty"]
    cart_res[item["item"]]["price"] = item["price"]
    cart_res[item["item"]]["total"] = cart_res[item["item"]]["qty"] * cart_res[item["item"]]["price"]

print(cart_res)

