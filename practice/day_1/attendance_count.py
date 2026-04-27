attendance = ["Present", "Absent", "Present", "Present", "Absent", "Absent"]

present_count = 0
absent_count = 0

for count in attendance:
    # print(count)
    if count == "Present":
        present_count += 1
    else:    
        absent_count += 1

print(present_count, absent_count)