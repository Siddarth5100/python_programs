'''
Q2. Remove Duplicate Cart Items
Covers: Lists

Scenario: A shopping cart got duplicate entries. Remove duplicates while preserving the original order.
cart = ['apple', 'bread', 'apple', 'milk', 'bread', 'eggs', 'milk']

Expected Output:
['apple', 'bread', 'milk', 'eggs']
'''

cart = ['apple', 'bread', 'apple', 'milk', 'bread', 'eggs', 'milk']

cart_1 = []

for item in cart:
    if item not in cart_1:
        cart_1.append(item)

print(cart_1)