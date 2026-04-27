'''
Q5. Training Attendance Comparison => Covers: Sets

Scenario: Two training sessions were conducted. Find common attendees, Session-1-only attendees,
and the combined attendee list.

session1 = ['Arun', 'Priya', 'Kumar', 'Divya', 'Raj']
session2 = ['Priya', 'Raj', 'Meena', 'Suresh', 'Arun']

Expected Output:
Attended Both
: {'Arun', 'Priya', 'Raj'}
Only Session 1 : {'Kumar', 'Divya'}
Attended Either : {'Arun', 'Priya', 'Kumar', 'Divya',
'Raj', 'Meena', 'Suresh'}
'''

session1 = ['Arun', 'Priya', 'Kumar', 'Divya', 'Raj']
session2 = ['Priya', 'Raj', 'Meena', 'Suresh', 'Arun']

attended_both = set()
one_session = set()
attended_either = set()

for attendee in session1:
    # print(attendee)
    if attendee in session2:
        # print(attendee)
        attended_both.add(attendee)
    
    one_session.add(attendee)

attended_either = session1.union(session2)

print(attended_both)
print(one_session)
print(attended_either)

'''
set() method usage error
'''