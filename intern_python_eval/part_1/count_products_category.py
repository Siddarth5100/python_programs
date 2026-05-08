'''
Q3. Count Products per Category
Covers: Dictionaries

Scenario: Given today's sales, count how many items sold in each category.

categories = ['electronics', 'clothing', 'electronics', 'food',
'clothing', 'electronics', 'food']

Expected Output:
{'electronics': 3, 'clothing': 2, 'food': 2}
'''

categories = ['electronics', 'clothing', 'electronics', 'food',
'clothing', 'electronics', 'food']

category_count = {}

for item in categories:
    # print(item)
    if item not in category_count:
        category_count[item] = 0
    category_count[item] += 1

print(category_count)