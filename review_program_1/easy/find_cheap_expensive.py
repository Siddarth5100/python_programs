'''
Q4. Cheapest & Most Expensive Product => Covers: Tuples

Scenario: Given a product catalog as tuples, find the cheapest and most expensive item.

products = [('Laptop', 55000), ('Mouse', 500), ('Keyboard', 1500),
('Monitor', 12000), ('Cable', 150)]

Expected Output:
Cheapest: ('Cable', 150)Most Expensive: ('Laptop', 55000)
'''

products = [('Laptop', 55000), ('Mouse', 500), ('Keyboard', 1500),
('Monitor', 12000), ('Cable', 150)]

most_expensive = ()
cheapest = ()

highest_amount = 0

for product in products:
    (device, price) = product

    if price > highest_amount:
        highest_amount = price
        most_expensive = product

print(most_expensive, cheapest)

'''
dint find the lowest one
'''