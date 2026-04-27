'''
Q9. Low-Stock Reorder Alert => Covers: Multi-structure

Scenario: After processing today's sales, identify items whose remaining stock falls at or below the
reorder level.

stock = {'apple': 100, 'banana': 50, 'milk': 30, 'bread': 25, 'eggs': 60}
reorder_level = {'apple': 20, 'banana': 15, 'milk': 10, 'bread': 10, 'eggs': 20}
sales = [('apple', 85), ('milk', 25), ('bread', 18),
('eggs', 35), ('banana', 30)]

Expected Output:
Remaining stock : {'apple': 15, 'banana': 20, 'milk': 5,
'bread': 7, 'eggs': 25}
Items to reorder: ['apple', 'milk', 'bread']
'''

stock = {'apple': 100, 'banana': 50, 'milk': 30, 'bread': 25, 
'eggs': 60}

reorder_level = {'apple': 20, 'banana': 15, 'milk': 10, 'bread': 10, 
'eggs': 20}

sales = [('apple', 85), ('milk', 25), ('bread', 18),
('eggs', 35), ('banana', 30)]

remaining_stock = {}
items_to_reorder = []

for key, val in stock.items():
    # print(key, val)
    if key not in remaining_stock:
        remaining_stock[key] = 0

    for sale in sales:
        # print(sale, type(sale))
        (item, qty) = sale
        # print(item, qty)
        if key == item:
            stock_bal = val - qty
            remaining_stock[key] = stock_bal

for item, qty in remaining_stock.items():
    # print(item, qty)
    for reorder_item, reorder_qty in reorder_level.items():
        # print(reorder_item, reorder_qty)
        if reorder_item == item:
            if qty < reorder_qty:
                items_to_reorder.append(item)

print(remaining_stock)
print(items_to_reorder)

'''
condition error for items_to_reorder
'''