'''
Q1. Employee Name Normalization
Covers: Strings

Scenario: HR receives names in inconsistent casing from different systems. 
Normalize them to proper title case.

names = "john DOE, JANE smith, Bob JOHNSON, alice WILLIAMS"

Expected Output:
['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Williams']
'''

names = "john DOE, JANE smith, Bob JOHNSON, alice WILLIAMS"

title_name = names.title()
name = title_name.split(",")
print(name)
# print(dir(str))

# 15:30