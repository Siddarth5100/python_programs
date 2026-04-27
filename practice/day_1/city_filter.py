cities = ["Chennai", "Delhi", "Mumbai", "Pune", "Goa"]

city_list = []

for city in cities:
    if len(city) > 5:
        city_list.append(city)

print(city_list)