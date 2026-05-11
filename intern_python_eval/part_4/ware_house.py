'''
3. Two warehouses stock items. 
Write a program to find items that are available in only one warehouse (not both).

warehouse_a = ["Pen", "Notebook", "Chair", "Monitor", "Desk", "Pen", "Chair"]
warehouse_b = ["Keyboard", "Monitor", "Mouse", "Chair", "Notebook"]

# Expected output: ['Desk', 'Keyboard', 'Mouse', 'Pen']
'''

warehouse_a = ["Pen", "Notebook", "Chair", "Monitor", "Desk", "Pen", "Chair"]
warehouse_b = ["Keyboard", "Monitor", "Mouse", "Chair", "Notebook"]

final_list = []


for item in warehouse_a:
    if item not in warehouse_b:
        if item not in final_list:
            final_list.append(item)

for items in warehouse_b:
    if items not in warehouse_a:
        if items not in final_list:
            final_list.append(items)

print(final_list)
