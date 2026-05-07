
inventory = {
    "Laptop": {"price": 50000, "stock": 4},
    "Mouse": {"price": 700, "stock": 10},
    "Keyboard": {"price": 1500, "stock": 0},
    "Monitor": {"price": 12000, "stock": 3}
}

'''
1. Print only products that are IN STOCK
Laptop - Stock: 4
'''

for item in inventory:
    if not inventory[item]["stock"] <= 0:
        # print(f"{item} - 'Stock': {inventory[item]["stock"]}")
        pass

'''
2. Find the MOST EXPENSIVE product
Most Expensive: Laptop - 50000
'''

expensive_product = ""
price = 0

for item in inventory:
    if inventory[item]["price"] > price:
        price = inventory[item]["price"]
        expensive_product = item
        # print(f"Most Expensive: {expensive_product} - {price}")

'''
3. Update stock after purchase

A customer buys:

2 Mouse
1 Monitor

Update inventory.
'''

mouse = 2
monitor = 1

for item in inventory:
    if item == "Mouse":
        inventory[item]["stock"] -= mouse
    if item == "Monitor":
        inventory[item]["stock"] -= monitor

# print(inventory)

'''
4. Delete OUT OF STOCK products

Meaning:
remove products where stock == 0
'''

del_stock = []
for item in inventory:
    if inventory[item]["stock"] == 0:
        del_stock.append(item)

for item in del_stock:
    inventory.pop(item)

'''
5. Print FINAL inventory
'''

print(inventory)