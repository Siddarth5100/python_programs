'''
Q6. Student Grade Analysis
Covers: Nested Dictionary

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
top_avg = 0
topper = ""

for mark in marks:
    if mark not in averages:
        averages[mark] = 0

    for key, val in marks[mark].items():
        averages[mark] += val / len(marks[mark])

for key, val in averages.items():
    if val > top_avg:
        top_avg = val
        topper = key

print(f"Averages: {averages}")
print(f"Topper: {topper} {(top_avg)}")

# 16:20
# 16:30