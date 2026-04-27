# ----------------------------------------que 4
'''
Two warehouses stock items.
Write a program to find items that are available in only one warehouse (not both).
'''

warehouse_a = ["Pen", "Notebook", "Chair", "Monitor", "Desk", "Pen", "Chair"]
warehouse_b = ["Keyboard", "Monitor", "Mouse", "Chair", "Notebook"]

# Expected output: ['Desk', 'Keyboard', 'Mouse', 'Pen']

items_avail = []

for items in warehouse_a:
    if items not in warehouse_b:
        if items not in items_avail:
            items_avail.append(items)

for items in warehouse_b:
    if items not in warehouse_a:
        if items not in items_avail:
            items_avail.append(items)

items_avail.sort()

print(items_avail)