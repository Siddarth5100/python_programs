'''
Build a small report system.

Your program should:

track customer spending,
identify highest spender,
detect repeated recharge amounts,
show customers whose total spending is above 500,
create a final structured summary dictionary.
'''

transactions = [
    ("Arun", 199),
    ("Bala", 399),
    ("Arun", 149),
    ("Charu", 249),
    ("Bala", 399),
    ("Deepa", 99),
    ("Arun", 199),
    ("Charu", 249),
]

# identify highest spender
highest_amount = 0
highest_spender = []
repeated_amount = {}

for transaction in transactions:
    (name, amount) = transaction
    if amount > highest_amount:
        highest_amount = amount
        highest_spender.append(name)

    # detect repeated recharge amounts
    if amount not in repeated_amount:
        repeated_amount[amount] = 0
    repeated_amount[amount] += 1
    
amount_repeat = []
for key, val in repeated_amount.items():
    if val > 1 and val not in amount_repeat:
        amount_repeat.append(key)

# show customers whose total spending is above 500
total_amount = {}
high_spender = []
for transaction in transactions:
    (name, amount) = transaction

    if name not in total_amount:
        total_amount[name] = 0
    total_amount[name] += amount

for key, val in total_amount.items():
    if val > 500:
        high_spender.append(key)