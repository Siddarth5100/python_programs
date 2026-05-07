'''
Requirements

Build a small analytics report.

Your program should identify and print:

total spending per customer
average order amount
highest spending customer
most ordered item
customers whose spending exceeds average spending
customer with highest average rating
final structured summary dictionary

Use:

list operations
dictionary operations
built-ins (sum, len, max, etc where useful)
nested traversal
calculations
conditions
'''

orders = [
    {
        "customer": "Arun",
        "items": ["Pizza", "Burger"],
        "amount": 450,
        "rating": 4.5
    },
    {
        "customer": "Bala",
        "items": ["Pizza"],
        "amount": 250,
        "rating": 3.8
    },
    {
        "customer": "Charu",
        "items": ["Burger", "Fries", "Coke"],
        "amount": 520,
        "rating": 4.9
    },
    {
        "customer": "Arun",
        "items": ["Coke"],
        "amount": 80,
        "rating": 4.0
    },
    {
        "customer": "Deepa",
        "items": ["Pizza", "Coke"],
        "amount": 300,
        "rating": 4.2
    }
]

total_spending = {}
# total spending per customer

item_count = {}
rating_total = 0

for order in orders:
    if order["customer"] not in total_spending:
        total_spending[order["customer"]] = 0
    total_spending[order["customer"]] += order["amount"]
# print(total_spending)

    rating_total += order["rating"]


    # most ordered item
    for item in order["items"]:
        if item not in item_count:
            item_count[item] = 0
        item_count[item] += 1
    
    print(order["rating"])
# print(item_count)
# print(rating_total)
avg_rating = rating_total / len(orders)
# print(avg_rating)

count = 0
item_most_ordered = []
# most ordered item
for key, val in item_count.items():
    if val >= count:
        count = val
        item_most_ordered.append(key)
# print(item_most_ordered)

# average order amount
total_amount = 0

# highest spending customer
amount = 0
customer_name = ""
for key, value in total_spending.items():
    total_amount += value
    if value > amount:
        amount = value
        customer_name = key
# print(customer_name)

avg_amount = total_amount / len(orders)
# print(avg_amount)

# customers whose spending exceeds average spending

# customer with highest average rating

# final structured summary dictionary