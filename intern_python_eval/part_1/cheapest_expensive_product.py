'''
Q4. Cheapest & Most Expensive Product
Covers: Tuples

Scenario: Given a product catalog as tuples, find the cheapest and most expensive item.

products = [('Laptop', 55000), ('Mouse', 500), ('Keyboard', 1500),
('Monitor', 12000), ('Cable', 150)]

Expected Output:
Cheapest: ('Cable', 150)Most Expensive: ('Laptop', 55000)
'''

cheapest_item = ()
most_expensive = ()
item_price = 0

products = [('Laptop', 55000), ('Mouse', 500), ('Keyboard', 1500),
('Monitor', 12000), ('Cable', 150)]

for product in products:
    (item, price) = product
    if price > item_price:
        item_price = price
        item_name = []
        item_name.append(item)
        item_name.append(price)
        most_expensive = item_name
    
    if price < item_price:
        item_price = price
        item_name = []
        item_name.append(item)
        item_name.append(price)
        cheapest_item = item_name
    
print(cheapest_item)
print(most_expensive)