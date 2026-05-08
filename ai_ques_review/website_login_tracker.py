'''
Build a small report.

Your program should:

count login frequency,
find most active user,
print users logged in only once,
remove duplicate users while preserving order,
create final summary dictionary.

Login Count:
Arun -> 3

Most Active:
Arun

Logged Once:
Charu
Deepa

Unique Users:
['Arun', 'Bala', 'Charu', 'Deepa']


'''

logins = [
    "Arun",
    "Bala",
    "Arun",
    "Charu",
    "Bala",
    "Arun",
    "Deepa"
]

login_frequency = {}

for name in logins:
    if name not in login_frequency:
        login_frequency[name] = 0
    login_frequency[name] += 1

print(login_frequency)

frequent_count = 0
user_name = ""
for name in login_frequency:
    if login_frequency[name] > frequent_count:
        frequent_count = login_frequency[name]
        user_name = name

print(frequent_count, user_name)

user_logged_once = []
for key, val in login_frequency.items():
    print(key, val)
    if val == 1:
        user_logged_once.append(key)

print(user_logged_once)

unique_user = []
for name in logins:
    print(name)
    if name not in unique_user:
        unique_user.append(name)

print(unique_user)