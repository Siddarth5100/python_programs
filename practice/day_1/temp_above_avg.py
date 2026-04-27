temps = [32, 35, 31, 30, 36, 34, 35]

temp_count = len(temps)
total_count = 0
days_count = 0

for temp in temps:
    total_count += temp

avg = round(total_count / temp_count, 2)

for temp in temps:
    if temp > avg:
        days_count += 1

print(days_count)

'''
we can use sum() here in total_count
'''