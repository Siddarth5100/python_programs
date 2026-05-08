'''
Q10. Customer Order Analytics
Covers: Complex — mixed structures

Scenario: Each order has multiple (product, qty, unit_price) items. Compute: (1) total revenue per
customer, (2) top 2 customers by revenue, (3) products from the master catalog that were never
ordered.

orders = [
{'customer': 'C1', 'items': [('P1', 2, 100), ('P2', 1, 500)]},
{'customer': 'C2', 'items': [('P1', 5, 100), ('P3', 2, 200)]},
{'customer': 'C1', 'items': [('P3', 3, 200)]},
{'customer': 'C3', 'items': [('P2', 4, 500)]}
]

all_products = ['P1', 'P2', 'P3', 'P4', 'P5']

Expected Output:
Revenue per customer : {'C1': 1300, 'C2': 900, 'C3': 2000}
Top 2 customers : [('C3', 2000), ('C1', 1300)]
Never ordered : ['P4', 'P5']
'''

orders = [
{'customer': 'C1', 'items': [('P1', 2, 100), ('P2', 1, 500)]},
{'customer': 'C2', 'items': [('P1', 5, 100), ('P3', 2, 200)]},
{'customer': 'C1', 'items': [('P3', 3, 200)]},
{'customer': 'C3', 'items': [('P2', 4, 500)]}
]

all_products = ['P1', 'P2', 'P3', 'P4', 'P5']

revenue_per_customer = {}
top_two_customers = []
never_ordered = []

ordered_product = []
highest_revenue = 0

for order in orders:
    if order["customer"] not in revenue_per_customer:
        revenue_per_customer[order["customer"]] = 0
    
    for product in order["items"]:
        (pro_id, qty, unit_price) = product
        revenue_per_customer[order["customer"]] += qty * unit_price

    for prod in order["items"]:
        (id, qty, unit_price) = prod
        if id not in ordered_product:
            ordered_product.append(id)

for pro in all_products:
    if pro not in ordered_product:
        never_ordered.append(pro)

print(revenue_per_customer)
print(never_ordered)

# 17:38
# 18:12 2 req not completed