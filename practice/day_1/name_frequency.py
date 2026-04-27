names = ["sid", "arun", "bala", "sid", "divya", "arun"]

name_dict = {}

for name in names:
    if name not in name_dict:
        name_dict[name] = 0
    
    name_dict[name] += 1

print(name_dict)