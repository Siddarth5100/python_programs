'''
Q6. Student Grade Analysis => Covers: Nested Dictionary

Scenario: Compute each student's average mark and identify the class topper.

marks = {
'Ravi': {'Math': 85, 'Science': 78, 'English': 92},
'Anita': {'Math': 90, 'Science': 88, 'English': 95},
'Kiran': {'Math': 70, 'Science': 75, 'English': 80}
}

Expected Output:
Averages: {'Ravi': 85.0, 'Anita': 91.0, 'Kiran': 75.0}
Topper : Anita (91.0)
'''

marks = {
'Ravi': {'Math': 85, 'Science': 78, 'English': 92},
'Anita': {'Math': 90, 'Science': 88, 'English': 95},
'Kiran': {'Math': 70, 'Science': 75, 'English': 80}
}

averages = {}
topper_avg = 0
topper_name = ""

for name in marks:
    # print(name)
    if name not in averages:
        averages[name] = 0    

    count = 0
    total_marks = 0

    for key, val in marks[name].items():
        # print(key, val)
        total_marks += val
        count += 1
    
    averages[name] = total_marks / count

for key, val in averages.items():
    if val > topper_avg:
        topper_avg = val
        topper_name = key

print(averages)
print(f"Student name: {topper_name}, scored: {topper_avg}")

'''
missed .items() in the last loop
'''