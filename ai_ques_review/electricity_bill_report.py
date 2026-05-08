'''
Each list = monthly electricity units for 3 months.

Your program should:
calculate total units per person
calculate average units
find highest electricity consumer
print users whose average usage exceeds 150
apply bill calculation:
first 100 units → ₹5/unit
remaining units → ₹8/unit
create final report dictionary

expected_out:
Arun -> Total: 365, Avg: 121.67

Highest Consumer: Deepa

High Usage Users:
Bala
Deepa
'''

units_data = {
    "Arun": [120, 135, 110],
    "Bala": [200, 180, 210],
    "Charu": [90, 95, 100],
    "Deepa": [300, 250, 280]
}

units_per_person = {}

for unit in units_data:
    if not unit in units_per_person:
        units_per_person[unit] = {"total_unit": 0}
    
    # total_units per person
    unit_total = 0
    for unit_val in units_data[unit]:
        unit_total += unit_val
    units_per_person[unit]["total_unit"] = unit_total

    for unit_val in units_data[unit]:
        if unit_val > 100:
            unit_cal = unit_val - 100
            total_unit_cal = (100 * 5) + (unit_cal * 8)
            units_per_person[unit]["total_unit_price"] = total_unit_cal
        else:
            total_unit_cal = unit_val * 5
            units_per_person[unit]["total_unit_price"] = total_unit_cal

# average_units
highest_total = 0
highest_consumer = ""
exceed_users = []

for total in units_per_person:
    avg = units_per_person[total]["total_unit"] / len(units_data["Arun"])
    units_per_person[total]["avg_unit"] = round(avg, 2)
    
    # find highest electricity consumer
    if units_per_person[total]["total_unit"] > highest_total:
        highest_total = units_per_person[total]["total_unit"]
        highest_consumer = total

    # print users whose average usage exceeds 150
    if units_per_person[total]["avg_unit"] > 150:
        exceed_users.append(total)

print(units_per_person)
print(highest_consumer, highest_total)
print(exceed_users)