words = ["cat", "dog", "cat", "bird", "dog", "lion"]

animal_name = {}

for name in words:
    # print(name)
    if not name in animal_name:
        animal_name[name] = 0
    if name in animal_name:
        animal_name[name] += 1

# print(animal_name)
count = 0
nam = []

for key, val in animal_name.items():
    print(key, val)
    if val == 1:
        nam.append(key)
            
print(nam)