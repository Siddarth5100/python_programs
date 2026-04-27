'''
Q3. Count Products per Category => Covers: Dictionaries

Scenario: Given today's sales, count how many items sold 
in each category.

categories = ['electronics', 'clothing', 'electronics', 'food',
'clothing', 'electronics', 'food']

Expected Output:
{'electronics': 3, 'clothing': 2, 'food': 2}
'''

categories = ['electronics', 'clothing', 'electronics', 'food',
'clothing', 'electronics', 'food']

# print(categories)

items_sold = {}

for category in categories:
    if category not in items_sold:
        # items_sold[category] = 1 
        '''
        initialized 1 instead of zero
        '''
        items_sold[category] = 0

    items_sold[category] += 1

print(items_sold)