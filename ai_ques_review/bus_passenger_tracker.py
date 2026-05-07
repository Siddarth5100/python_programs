logs = [
    ("Arun", "IN"),
    ("Bala", "IN"),
    ("Arun", "OUT"),
    ("Charu", "IN"),
    ("Bala", "OUT"),
    ("Deepa", "IN"),
    ("Charu", "OUT")
]

'''
1. Find who is CURRENTLY inside the bus
Deepa
'''

inside_bus = []

for log in logs:
    (name, status) = log
    if status == "IN":
        inside_bus.append(name)
    elif status == "OUT":
        inside_bus.remove(name)

# print(inside_bus)

'''
2. Count total IN entries
Total IN: 4
'''

count_in = 0

for log in logs:
    (name, status) = log

    if status == "IN":
        count_in += 1

# print(count_in)

'''
3. Find people who entered but never exited
Deepa
'''

in_bus = {}

for log in logs:
    (name, status) = log
    
    if name not in in_bus:
        in_bus[name] = {"IN": 0, "OUT": 0}
    
    if status == "IN":
        in_bus[name]["IN"] += 1
    elif status == "OUT":
        in_bus[name]["OUT"] += 1
  
for key, val in in_bus.items():
    if val["OUT"] == 0:
        # print(key)
        pass

'''
4. Create final status dictionary
{
    "Arun": "OUT",
    "Bala": "OUT",
    "Deepa": "IN"
}
'''

final_status = {}
for log in logs:
    # print(log)
    (name, status) = log
    if name not in final_status:
        final_status[name] = ""
    
    if status == "IN":
        final_status[name] = status
    elif status == "OUT":
        final_status[name] = status

# print(final_status)