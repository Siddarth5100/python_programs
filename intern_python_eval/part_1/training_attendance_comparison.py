'''
Q5. Training Attendance Comparison
Covers: Sets

Scenario: Two training sessions were conducted. Find common attendees, Session-1-only attendees,
and the combined attendee list.

session1 = ['Arun', 'Priya', 'Kumar', 'Divya', 'Raj']
session2 = ['Priya', 'Raj', 'Meena', 'Suresh', 'Arun']

Expected Output:

Attended Both : {'Arun', 'Priya', 'Raj'}
Only Session 1 : {'Kumar', 'Divya'}
Attended Either : {'Arun', 'Priya', 'Kumar', 'Divya', 'Raj', 'Meena', 'Suresh'}
'''

session1 = ['Arun', 'Priya', 'Kumar', 'Divya', 'Raj']
session2 = ['Priya', 'Raj', 'Meena', 'Suresh', 'Arun']

attended_both = set()
only_session_1 = set()
attended_either = set()

for attendee in session1:
    for name in session2:
        if attendee == name:
            attended_both.add(attendee)
        
print(attended_both)

# 15:30
# 16:15