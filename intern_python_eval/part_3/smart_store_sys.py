'''
Mixed Python Logic Drill
⏱️ Suggested Time: 35 to 45 mins

This question combines:

list
dict
list of dict
dict of list
nested traversal
calculations
conditions
aggregation
filtering
logical thinking

1. Total spending per customer

{
    "Arun": 51400
}

'''

orders = [
    {
        "customer": "Arun",
        "items": [
            {"name": "Laptop", "price": 50000, "qty": 1},
            {"name": "Mouse", "price": 700, "qty": 2}
        ],
        "ratings": [4, 5, 4]
    },
    {
        "customer": "Bala",
        "items": [
            {"name": "Keyboard", "price": 1500, "qty": 1},
            {"name": "Mouse", "price": 700, "qty": 1}
        ],
        "ratings": [3, 4]
    },
    {
        "customer": "Charu",
        "items": [
            {"name": "Laptop", "price": 50000, "qty": 1},
            {"name": "Monitor", "price": 12000, "qty": 2}
        ],
        "ratings": [5, 5, 4]
    },
    {
        "customer": "Deepa",
        "items": [
            {"name": "Mouse", "price": 700, "qty": 5}
        ],
        "ratings": [4]
    }
]

customer_total_cal = {}

item_cal = {}

highest_spending_cus = ""
high_amount = 0

most_purchased_item = ""
purchased_qty = 0



for order in orders:
    if order["customer"] not in customer_total_cal:
        customer_total_cal[order["customer"]] = {"total": 0}
    
    for item in order["items"]:    
        if item["name"] not in item_cal:
            item_cal[item["name"]] = 0
        item_cal[item["name"]] += item["qty"]

        customer_total_cal[order["customer"]]["total"] += item["price"] * item["qty"] 

    count_ratings = 0
    count = 0
    for rating in order["ratings"]:
        count_ratings += rating
        
        count += 1

    avg = count_ratings / count

for total in customer_total_cal:
    if customer_total_cal[total]["total"] > high_amount:
        high_amount = customer_total_cal[total]["total"]
        highest_spending_cus = total

for key, val in item_cal.items():
    if val > purchased_qty:
        purchased_qty = val
        most_purchased_item = key

print(customer_total_cal)
print(high_amount, highest_spending_cus)
print(most_purchased_item, purchased_qty)