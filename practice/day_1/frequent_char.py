'''
Find most frequent character
'''
word = "banana"

frequent_char = ""
count = {}

for letter in word:
    # print(letter)
    if not letter in count:
        count[letter] = 0
# print(count)
        for char in word:
            if letter == char:
                count[letter] += 1
# print(count)

# expec_output => {'b': 1, 'a': 3, 'n': 2}

check_val_count = 0
for key, val in count.items():
    # print(key, val)
    if val > check_val_count:
        check_val_count = val
        frequent_char = key

print(frequent_char, check_val_count)